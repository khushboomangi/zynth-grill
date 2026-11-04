import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Zynth Grill - Food Delivery",
    page_icon="🍔",
    layout="wide"
)

# Cache data taake file bar bar read na ho aur app fast chale
@st.cache_data
def load_html_file():
    html_file_path = "index.html"
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

html_code = load_html_file()

if html_code:
    # Render HTML inside Streamlit component
    st.components.v1.html(html_code, height=950, scrolling=True)
else:
    st.error("Error: index.html file not found in the repository!")
