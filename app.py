import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Zynth Grill - Food Delivery",
    page_icon="🍔",
    layout="wide"
)

# Read index.html file
html_file_path = "index.html"

if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Render HTML inside Streamlit component
    st.components.v1.html(html_code, height=950, scrolling=True)
else:
    st.error("Error: index.html file not found in the repository!")
