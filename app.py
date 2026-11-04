import streamlit as st
import os

# Page configuration
st.set_page_config(
    page_title="Zynth Grill - Food Delivery",
    page_icon="🍔",
    layout="wide"
)

# Sidebar mein Social Links (Jo 100% naye tab mein khulenge bina kisi error ke)
with st.sidebar:
    st.image("https://img.icons8.com/color/96/hamburger.png", width=80)
    st.title("Zynth Grill")
    st.markdown("The Ultimate Taste of Nawabshah")
    st.divider()
    
    st.subheader("Connect With Us")
    st.markdown("[💬 Chat on WhatsApp (03093009181)](https://wa.me/923093009181)")
    st.markdown("[📸 Instagram (@khushboo.mangi)](https://www.instagram.com/khushboo.mangi/)")

# Cache data taake SPA fast chale
@st.cache_data
def load_html_file():
    html_file_path = "index.html"
    if os.path.exists(html_file_path):
        with open(html_file_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

html_code = load_html_file()

if html_code:
    # Render main HTML SPA inside Streamlit component
    st.components.v1.html(html_code, height=950, scrolling=True)
else:
    st.error("Error: index.html file not found in the repository!")
