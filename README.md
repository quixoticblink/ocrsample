# Image Data Extractor

A small Streamlit app that reads any image (PNG, JPG, JPEG, WEBP, BMP, TIFF),
uses [Docling](https://github.com/DS4SD/docling) to detect and parse both
**tables** and **plain text**, and lets you download the results as Excel and
text files.

## Features

- Accepts PNG, JPG, JPEG, WEBP, BMP, TIFF
- Drag-and-drop **batch upload** of multiple files
- **Two-column layout per image**: original image on the left, extracted
  content (tables + text) on the right
- Per-file downloads (XLSX of tables, MD/TXT of full text) directly beneath
  each image
- Combined downloads at the bottom: single XLSX of all tables, plus a ZIP
  with per-file XLSX and text files
- Works equally well for table snippets and text-heavy document images

## Setup

Requires Python 3.10+.

```bash
cd png-table-extractor
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

The first run downloads Docling's layout/table models (a few hundred MB).
Subsequent runs are much faster — models are cached on disk.

## Run

```bash
streamlit run app.py
```

Streamlit prints a local URL (usually http://localhost:8501). Open it in your
browser, drop in your PNG files, click **Extract tables**, and download the
resulting `.xlsx`.

## How it works

1. Each uploaded PNG is written to a temp file and passed to Docling's
   `DocumentConverter`.
2. Docling returns a structured document. The app iterates over
   `document.tables` and converts each to a pandas `DataFrame`
   via `table.export_to_dataframe()`.
3. All DataFrames are written into a single `openpyxl` workbook, one per sheet,
   with sheet names derived from the source filename.

## Troubleshooting

- **Model download is slow / offline:** Docling caches models under
  `~/.cache/docling`. Pre-warm on a machine with internet, then copy the cache.
- **No tables detected:** some scans have low contrast or skew. Try
  straightening/cropping the image. The app will still show Docling's markdown
  output so you can see what it read.
- **Sheet name collisions:** the app automatically truncates and de-duplicates
  sheet names to satisfy Excel's 31-char limit.

## Files

- `app.py` — Streamlit UI + extraction pipeline
- `requirements.txt` — Python dependencies
