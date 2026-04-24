"""
IBM Carbon Design System theme for Streamlit.
Inject via: st.markdown(CARBON_CSS, unsafe_allow_html=True)
"""

CARBON_CSS = """
<style>
/* ── IBM Plex Sans font ── */
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Carbon Color Tokens ── */
:root {
    --cds-background: #ffffff;
    --cds-layer-01: #f4f4f4;
    --cds-layer-02: #e0e0e0;
    --cds-layer-hover: #e8e8e8;
    --cds-text-primary: #161616;
    --cds-text-secondary: #525252;
    --cds-text-placeholder: #a8a8a8;
    --cds-text-on-color: #ffffff;
    --cds-link-primary: #0f62fe;
    --cds-link-hover: #0043ce;
    --cds-border-subtle: #e0e0e0;
    --cds-border-strong: #8d8d8d;
    --cds-button-primary: #0f62fe;
    --cds-button-primary-hover: #0043ce;
    --cds-button-secondary: #393939;
    --cds-button-danger: #da1e28;
    --cds-support-error: #da1e28;
    --cds-support-success: #198038;
    --cds-support-warning: #f1c21b;
    --cds-support-info: #0043ce;
    --cds-focus: #0f62fe;
    --cds-overlay: rgba(22, 22, 22, 0.5);
    --cds-spacing-03: 0.5rem;
    --cds-spacing-05: 1rem;
    --cds-spacing-07: 2rem;
}

/* ── Global Reset ── */
html, body, [data-testid="stAppViewContainer"],
[data-testid="stApp"], .main, .block-container {
    font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--cds-text-primary) !important;
}

.block-container {
    max-width: 1584px !important;  /* Carbon max breakpoint */
    padding: 2rem 2rem 4rem 2rem !important;
}

/* ── Header Area ── */
[data-testid="stAppViewContainer"] > .main > .block-container > div:first-child {
    border-bottom: 1px solid var(--cds-border-subtle);
    margin-bottom: 1.5rem;
}

/* ── Typography ── */
h1 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 2rem !important;
    letter-spacing: -0.02em !important;
    color: var(--cds-text-primary) !important;
    line-height: 1.25 !important;
    margin-bottom: 0.25rem !important;
}

h2, [data-testid="stSubheader"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.25rem !important;
    color: var(--cds-text-primary) !important;
    letter-spacing: -0.01em !important;
}

h3 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1.1rem !important;
    color: var(--cds-text-primary) !important;
}

p, span, label, div {
    font-family: 'IBM Plex Sans', sans-serif !important;
}

[data-testid="stCaptionContainer"] {
    font-size: 0.875rem !important;
    color: var(--cds-text-secondary) !important;
    line-height: 1.4 !important;
    max-width: 640px;
}

/* ── Primary Button ── */
[data-testid="stButton"] > button[kind="primary"],
button[kind="primary"] {
    background-color: var(--cds-button-primary) !important;
    color: var(--cds-text-on-color) !important;
    border: none !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    letter-spacing: 0.01em !important;
    padding: 0.75rem 4rem 0.75rem 1rem !important;
    min-height: 48px !important;
    transition: background-color 110ms cubic-bezier(0.2, 0, 0.38, 0.9) !important;
    text-transform: none !important;
}

[data-testid="stButton"] > button[kind="primary"]:hover,
button[kind="primary"]:hover {
    background-color: var(--cds-button-primary-hover) !important;
}

[data-testid="stButton"] > button[kind="primary"]:focus {
    outline: 2px solid var(--cds-focus) !important;
    outline-offset: -2px !important;
    box-shadow: inset 0 0 0 1px var(--cds-focus) !important;
}

/* ── Secondary / Default Buttons ── */
[data-testid="stButton"] > button:not([kind="primary"]),
[data-testid="stDownloadButton"] > button {
    background-color: var(--cds-layer-01) !important;
    color: var(--cds-text-primary) !important;
    border: 1px solid var(--cds-border-subtle) !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    padding: 0.625rem 1rem !important;
    min-height: 40px !important;
    transition: background-color 110ms cubic-bezier(0.2, 0, 0.38, 0.9) !important;
}

[data-testid="stButton"] > button:not([kind="primary"]):hover,
[data-testid="stDownloadButton"] > button:hover {
    background-color: var(--cds-layer-hover) !important;
    border-color: var(--cds-border-strong) !important;
}

/* Download buttons with primary type */
[data-testid="stDownloadButton"] > button[kind="primary"] {
    background-color: var(--cds-button-primary) !important;
    color: var(--cds-text-on-color) !important;
    border: none !important;
}

[data-testid="stDownloadButton"] > button[kind="primary"]:hover {
    background-color: var(--cds-button-primary-hover) !important;
}

/* ── File Uploader ── */
[data-testid="stFileUploader"] {
    border: 2px dashed var(--cds-border-subtle) !important;
    border-radius: 0 !important;
    padding: 1.5rem !important;
    background: var(--cds-layer-01) !important;
    transition: border-color 150ms ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: var(--cds-border-strong) !important;
}

[data-testid="stFileUploader"] label {
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    color: var(--cds-text-secondary) !important;
}

[data-testid="stFileUploader"] button {
    border-radius: 0 !important;
    background-color: var(--cds-button-primary) !important;
    color: white !important;
    border: none !important;
}

/* ── Tabs (Carbon style) ── */
[data-testid="stTabs"] [data-baseweb="tab-list"] {
    gap: 0 !important;
    border-bottom: 2px solid var(--cds-border-subtle) !important;
}

[data-testid="stTabs"] [data-baseweb="tab"] {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    color: var(--cds-text-secondary) !important;
    border-radius: 0 !important;
    padding: 0.75rem 1rem !important;
    border-bottom: 3px solid transparent !important;
    transition: all 110ms ease !important;
    background: transparent !important;
}

[data-testid="stTabs"] [data-baseweb="tab"]:hover {
    color: var(--cds-text-primary) !important;
    background: var(--cds-layer-hover) !important;
}

[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] {
    color: var(--cds-text-primary) !important;
    font-weight: 600 !important;
    border-bottom: 3px solid var(--cds-button-primary) !important;
}

/* ── Data Tables ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--cds-border-subtle) !important;
    border-radius: 0 !important;
}

[data-testid="stDataFrame"] table {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.875rem !important;
}

/* ── Alerts / Notifications ── */
[data-testid="stAlert"] {
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-size: 0.875rem !important;
    border-left: 3px solid !important;
    padding: 1rem !important;
}

div[data-testid="stAlert"][data-baseweb*="info"],
div[role="alert"]:has(.st-emotion-cache-info) {
    background: #edf5ff !important;
    border-left-color: var(--cds-support-info) !important;
}

div[data-testid="stAlert"][data-baseweb*="success"],
.stSuccess {
    background: #defbe6 !important;
    border-left-color: var(--cds-support-success) !important;
}

div[data-testid="stAlert"][data-baseweb*="warning"],
.stWarning {
    background: #fcf4d6 !important;
    border-left-color: var(--cds-support-warning) !important;
}

div[data-testid="stAlert"][data-baseweb*="error"],
.stError {
    background: #fff1f1 !important;
    border-left-color: var(--cds-support-error) !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    border: 1px solid var(--cds-border-subtle) !important;
    border-radius: 0 !important;
    background: var(--cds-background) !important;
}

[data-testid="stExpander"] summary {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    padding: 0.75rem 1rem !important;
}

/* ── Progress Bar ── */
[data-testid="stProgress"] > div > div {
    background-color: var(--cds-layer-02) !important;
    border-radius: 0 !important;
    height: 4px !important;
}

[data-testid="stProgress"] > div > div > div {
    background-color: var(--cds-button-primary) !important;
    border-radius: 0 !important;
}

/* ── Text Area ── */
[data-testid="stTextArea"] textarea {
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 0.8125rem !important;
    border-radius: 0 !important;
    border: 1px solid var(--cds-border-subtle) !important;
    background: var(--cds-layer-01) !important;
}

[data-testid="stTextArea"] textarea:focus {
    border-color: var(--cds-focus) !important;
    outline: 2px solid var(--cds-focus) !important;
    outline-offset: -2px !important;
}

/* ── Dividers ── */
hr {
    border: none !important;
    border-top: 1px solid var(--cds-border-subtle) !important;
    margin: 1.5rem 0 !important;
}

/* ── Image containers ── */
[data-testid="stImage"] {
    border: 1px solid var(--cds-border-subtle);
    background: var(--cds-layer-01);
    padding: 0.5rem;
}

/* ── Scrollbar styling ── */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track { background: var(--cds-layer-01); }
::-webkit-scrollbar-thumb {
    background: var(--cds-border-strong);
    border-radius: 0;
}

/* ── Caption / small text ── */
.stCaption, [data-testid="stCaption"] {
    color: var(--cds-text-secondary) !important;
    font-size: 0.75rem !important;
    letter-spacing: 0.02em !important;
}

/* ── Hide Streamlit branding ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] {
    background: var(--cds-background) !important;
    border-bottom: 1px solid var(--cds-border-subtle) !important;
}
</style>
"""
