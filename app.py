"""
Image Data Extractor
--------------------
A Streamlit app that extracts tabular data AND full text from any image
(PNG, JPG, JPEG, WEBP, BMP, TIFF) using Docling.

Layout per uploaded image:
    [ Original image on the left ]  |  [ Extracted tables + text on the right ]
    [ Download buttons below    ]

Run:
    streamlit run app.py
"""

from __future__ import annotations

import os

# Redirect model caches to writable directories (Streamlit Cloud has a
# read-only venv, so torch/HF can't write to site-packages).
os.environ.setdefault("HF_HOME", "/tmp/hf_home")
os.environ.setdefault("TORCH_HOME", "/tmp/torch_home")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/cache")

import io
import re
import tempfile
import zipfile
from pathlib import Path
from typing import List, Tuple

import pandas as pd
import streamlit as st
from PIL import Image

from carbon_theme import CARBON_CSS


SUPPORTED_TYPES = ["png", "jpg", "jpeg", "webp", "bmp", "tif", "tiff"]


# ---------- Docling (loaded lazily so Streamlit boots fast) ---------- #

@st.cache_resource(show_spinner="Loading Docling models (first run downloads weights)...")
def get_docling_converter():
    """Instantiate and cache the Docling DocumentConverter.

    Uses Tesseract OCR instead of RapidOCR to avoid permission errors
    on Streamlit Cloud (RapidOCR tries to write models into the
    read-only venv).
    """
    from docling.document_converter import DocumentConverter
    from docling.datamodel.pipeline_options import PipelineOptions

    pipeline_opts = PipelineOptions()

    # Try to use Tesseract; fall back to default if unavailable
    try:
        from docling.datamodel.pipeline_options import TesseractOcrOptions
        pipeline_opts.ocr_options = TesseractOcrOptions()
    except ImportError:
        pass  # Use default OCR (works locally where venv is writable)

    return DocumentConverter(pipeline_options=pipeline_opts)


# ---------- Extraction ---------- #

def extract_from_image(img_bytes: bytes, filename: str) -> Tuple[List[pd.DataFrame], str]:
    """
    Run Docling on a single image and return (tables, markdown_text).

    - tables: list of pandas DataFrames, one per detected table.
    - markdown_text: the full document rendered as markdown. This is the
      plain-text extraction that works for text-heavy images where no tables
      are present.
    """
    converter = get_docling_converter()

    suffix = Path(filename).suffix or ".png"
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(img_bytes)
        tmp_path = tmp.name

    try:
        result = converter.convert(tmp_path)
        doc = result.document

        tables: List[pd.DataFrame] = []
        for table in getattr(doc, "tables", []) or []:
            df = None
            try:
                df = table.export_to_dataframe()
            except Exception:
                try:
                    df = pd.DataFrame(table.export_to_dict().get("data", []))
                except Exception:
                    df = None
            if df is not None and not df.empty:
                tables.append(df)

        try:
            md = doc.export_to_markdown()
        except Exception:
            md = ""

        return tables, md
    finally:
        try:
            Path(tmp_path).unlink(missing_ok=True)
        except Exception:
            pass


# ---------- Utilities ---------- #

_SAFE = re.compile(r"[^A-Za-z0-9_]+")


def safe_sheet_name(name: str, index: int, existing: set) -> str:
    """Excel sheet names: <=31 chars, no []:*?/\\ and must be unique."""
    base = _SAFE.sub("_", Path(name).stem)[:24] or "Sheet"
    candidate = f"{base}_{index}"
    n = 1
    final = candidate[:31]
    while final in existing:
        final = f"{candidate[:28]}_{n}"[:31]
        n += 1
    existing.add(final)
    return final


def dataframes_to_xlsx(named_tables: List[Tuple[str, pd.DataFrame]]) -> bytes:
    """Write a list of (sheet_name, df) to an in-memory xlsx file."""
    buf = io.BytesIO()
    with pd.ExcelWriter(buf, engine="openpyxl") as writer:
        if not named_tables:
            pd.DataFrame({"info": ["No tables were extracted."]}).to_excel(
                writer, sheet_name="Info", index=False
            )
        else:
            for sheet, df in named_tables:
                df.to_excel(writer, sheet_name=sheet, index=False)
    buf.seek(0)
    return buf.read()


def build_combined_zip(
    per_file_results: List[dict],
    combined_xlsx: bytes,
) -> bytes:
    """Bundle every file's xlsx + text, plus a combined xlsx, into one zip."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("combined_tables.xlsx", combined_xlsx)
        for r in per_file_results:
            stem = Path(r["name"]).stem
            if r["xlsx"] is not None:
                zf.writestr(f"{stem}/{stem}_tables.xlsx", r["xlsx"])
            zf.writestr(f"{stem}/{stem}_text.md", r["md"] or "")
    buf.seek(0)
    return buf.read()


# ---------- Streamlit UI ---------- #

def render_result_row(idx: int, result: dict):
    """Render the two-column row for a single image result."""
    st.markdown(f"### {result['name']}")

    left, right = st.columns(2, gap="large")

    # ---------- LEFT: original image ---------- #
    with left:
        st.markdown("**Original image**")
        try:
            st.image(result["image"], use_container_width=True)
        except Exception:
            st.warning("Could not render preview.")

    # ---------- RIGHT: extracted content ---------- #
    with right:
        st.markdown("**Extracted content**")

        tables: List[pd.DataFrame] = result["tables"]
        md: str = result["md"] or ""

        tab_labels = []
        if tables:
            tab_labels.append(f"Tables ({len(tables)})")
        tab_labels.append("Text")

        tabs = st.tabs(tab_labels)

        if tables:
            with tabs[0]:
                for t_i, df in enumerate(tables, start=1):
                    st.caption(f"Table {t_i} — {df.shape[0]} rows × {df.shape[1]} cols")
                    st.dataframe(df, use_container_width=True, height=min(320, 40 + 28 * (len(df) + 1)))
            text_tab = tabs[1]
        else:
            text_tab = tabs[0]

        with text_tab:
            if md.strip():
                st.text_area(
                    label="Extracted text (markdown)",
                    value=md,
                    height=380,
                    key=f"text_{idx}",
                    label_visibility="collapsed",
                )
            else:
                st.info("No text extracted.")

    # ---------- Download buttons below ---------- #
    dl_cols = st.columns(3)
    stem = Path(result["name"]).stem

    with dl_cols[0]:
        if result["xlsx"] is not None:
            st.download_button(
                label="⬇️ Download tables (.xlsx)",
                data=result["xlsx"],
                file_name=f"{stem}_tables.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key=f"dl_xlsx_{idx}",
                use_container_width=True,
            )
        else:
            st.button("No tables to download", disabled=True,
                      key=f"dl_xlsx_disabled_{idx}", use_container_width=True)

    with dl_cols[1]:
        st.download_button(
            label="⬇️ Download text (.md)",
            data=(result["md"] or "").encode("utf-8"),
            file_name=f"{stem}_text.md",
            mime="text/markdown",
            key=f"dl_md_{idx}",
            use_container_width=True,
            disabled=not (result["md"] or "").strip(),
        )

    with dl_cols[2]:
        st.download_button(
            label="⬇️ Download text (.txt)",
            data=(result["md"] or "").encode("utf-8"),
            file_name=f"{stem}_text.txt",
            mime="text/plain",
            key=f"dl_txt_{idx}",
            use_container_width=True,
            disabled=not (result["md"] or "").strip(),
        )

    st.divider()


def main():
    st.set_page_config(
        page_title="Image Data Extractor",
        page_icon="📊",
        layout="wide",
    )

    # Inject Carbon Design System styles
    st.markdown(CARBON_CSS, unsafe_allow_html=True)

    st.title("Image Data Extractor")
    st.caption(
        "Upload one or more images (PNG, JPG, JPEG, WEBP, BMP, TIFF). "
        "Docling extracts tables and full text — works for both table snippets "
        "and text-heavy documents."
    )

    uploaded = st.file_uploader(
        "Drop images here",
        type=SUPPORTED_TYPES,
        accept_multiple_files=True,
        help="Batch upload is supported. Each image gets its own side-by-side view.",
    )

    run = st.button("Extract data", type="primary", disabled=not uploaded)

    if not uploaded:
        st.info("Upload at least one image to get started.")
        return

    if not run:
        # Show a lightweight preview grid before extraction so the user knows
        # which files are queued.
        with st.expander(f"Queued ({len(uploaded)} file(s))", expanded=False):
            cols = st.columns(min(4, len(uploaded)))
            for i, f in enumerate(uploaded):
                with cols[i % len(cols)]:
                    try:
                        st.image(Image.open(f), caption=f.name, use_container_width=True)
                    except Exception:
                        st.write(f.name)
                    f.seek(0)
        return

    # ---------- Run extraction ---------- #
    progress = st.progress(0.0, text="Starting…")
    per_file_results: List[dict] = []
    combined_named_tables: List[Tuple[str, pd.DataFrame]] = []
    combined_names: set = set()

    for idx, f in enumerate(uploaded, start=1):
        progress.progress((idx - 1) / len(uploaded),
                          text=f"Processing {f.name} ({idx}/{len(uploaded)})")
        img_bytes = f.read()

        # Load once for preview re-use
        try:
            pil_img = Image.open(io.BytesIO(img_bytes)).copy()
        except Exception:
            pil_img = None

        try:
            tables, md = extract_from_image(img_bytes, f.name)
        except Exception as e:
            st.error(f"❌ {f.name}: extraction failed — {e}")
            per_file_results.append({
                "name": f.name, "image": pil_img, "tables": [],
                "md": "", "xlsx": None,
            })
            continue

        # Per-file xlsx (only if we have tables)
        per_file_xlsx = None
        if tables:
            local_existing: set = set()
            local_named = [
                (safe_sheet_name(f.name, i + 1, local_existing), df)
                for i, df in enumerate(tables)
            ]
            per_file_xlsx = dataframes_to_xlsx(local_named)

            # Also contribute to the combined workbook
            for i, df in enumerate(tables, start=1):
                sheet = safe_sheet_name(f.name, i, combined_names)
                combined_named_tables.append((sheet, df))

        per_file_results.append({
            "name": f.name,
            "image": pil_img,
            "tables": tables,
            "md": md,
            "xlsx": per_file_xlsx,
        })

    progress.progress(1.0, text="Done")
    st.success(
        f"Processed {len(per_file_results)} image(s). "
        f"Total tables extracted: {sum(len(r['tables']) for r in per_file_results)}."
    )
    st.divider()

    # ---------- Render per-file two-column layout ---------- #
    for idx, r in enumerate(per_file_results):
        render_result_row(idx, r)

    # ---------- Combined downloads at the bottom ---------- #
    st.subheader("Download all results")

    combined_xlsx_bytes = dataframes_to_xlsx(combined_named_tables)
    zip_bytes = build_combined_zip(per_file_results, combined_xlsx_bytes)

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="⬇️ Combined tables (.xlsx)",
            data=combined_xlsx_bytes,
            file_name="extracted_tables.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
            type="primary",
        )
    with col2:
        st.download_button(
            label="⬇️ All results (.zip — xlsx + text per file)",
            data=zip_bytes,
            file_name="extracted_results.zip",
            mime="application/zip",
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
