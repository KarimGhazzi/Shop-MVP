# app.py
import streamlit as st
from scraper import scrape_mytheresa

st.title("🛍️ Mytheresa Scraper (ShopQuick MVP)")

if st.button("Scrape Mytheresa"):
    st.info("Scraping...")
    items = scrape_mytheresa()
    st.success(f"Found {len(items)} items")

    for item in items:
        st.image(item['image_url'], width=200)
        st.write(f"**{item['name']}**")
        st.write(f"💰 {item['price']}")
        st.markdown("---")