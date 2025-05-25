import streamlit as st
from scraper import scrape_items
from gpt_api import generate_description

st.title("🛒 ShopQuick - Smart Retail Scraper")

url = st.text_input("Enter a product page URL:")
if url:
    items = scrape_items(url)
    for item in items:
        st.image(item['image_url'], width=150)
        st.subheader(item['name'])
        if st.button(f"Describe {item['name']}", key=item['name']):
            description = generate_description(item['image_url'])
            st.write(description)