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
    --cds-text-on-color: #ffffff;
    --cds-border-subtle: #e0e0e0;
    --cds-border-strong: #8d8d8d;
    --cds-button-primary: #0f62fe;
    --cds-button-primary-hover: #0043ce;
    --cds-support-error: #da1e28;
    --cds-support-success: #198038;
    --cds-support-warning: #f1c21b;
    --cds-support-info: #0043ce;
    --cds-focus: #0f62fe;
}

/* ── Global font ── */
html, body, [data-testid="stAppViewContainer"], .main {
    font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.block-container {
    max-width: 1584px !important;
    padding: 2rem 2rem 4rem 2rem !important;
}

/* ── Typography ── */
h1 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 2rem !important;
    letter-spacing: -0.02em !important;
    color: var(--cds-text-primary) !important;
    line-height: 1.25 !important;
}

h2 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1.25rem !important;
    color: var(--cds-text-primary) !important;
}

h3 {
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 1.1rem !important;
    color: var(--cds-text-primary) !important;
}

[data-testid="stCaptionContainer"] {
    font-size: 0.875rem !important;
    color: var(--cds-text-secondary) !important;
    line-height: 1.5 !important;
}

/* ── Primary Button ── */
[data-testid="stButton"] > button[kind="primary"] {
    background-color: var(--cds-button-primary) !important;
    color: var(--cds-text-on-color) !important;
    border: none !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    padding: 0.75rem 2rem !important;
    min-height: 48px !important;
    transition: background-color 110ms ease !important;
}

[data-testid="stButton"] > button[kind="primary"]:hover {
    background-color: var(--cds-button-primary-hover) !important;
}

/* ── Secondary Buttons ── */
[data-testid="stButton"] > button:not([kind="primary"]) {
    background-color: var(--cds-layer-01) !important;
    color: var(--cds-text-primary) !important;
    border: 1px solid var(--cds-border-subtle) !important;
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    min-height: 40px !important;
    transition: background-color 110ms ease !important;
}

[data-testid="stButton"] > button:not([kind="primary"]):hover {
    background-color: var(--cds-layer-hover) !important;
}

/* ── Download Buttons ── */
[data-testid="stDownloadButton"] > button {
    border-radius: 0 !important;
    font-family: 'IBM Plex Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    min-height: 40px !important;
}

[data-testid="stDownloadButton"] > button[kind="primary"] {
    background-color: var(--cds-button-primary) !important;
    color: var(--cds-text-on-color) !important;
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

/* ── Alerts ── */
[data-testid="stAlert"] {
    border-radius: 0 !important;
    border-left: 3px solid !important;
}

/* ── Expander ── */
[data-testid="stExpander"] {
    border: 1px solid var(--cds-border-subtle) !important;
    border-radius: 0 !important;
}

/* ── Progress Bar ── */
[data-testid="stProgress"] > div > div {
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
    padding: 0.5rem;
}

/* ── Hide Streamlit branding ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
</style>
"""
