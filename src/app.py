# app.py

import streamlit as st
from scraper import scrape_mytheresa

st.set_page_config(page_title="ShopQuick - Mytheresa Scraper", layout="centered")

st.title("🛍️ ShopQuick - Mytheresa.com Scraper")
st.markdown("This app scrapes [Mytheresa.com](https://www.mytheresa.com/en-de/men/shoes.html) and shows product names, prices, and images.")

if st.button("Scrape Mytheresa"):
    st.info("Scraping, please wait...")
    try:
        items = scrape_mytheresa()
        st.success(f"Found {len(items)} items")

        for item in items:
            st.image(item['image_url'], width=250)
            st.markdown(f"**{item['name']}**")
            st.markdown(f"💰 **Price:** {item['price']}")
            st.markdown("---")
    except Exception as e:
        st.error("An error occurred while scraping.")
        st.exception(e)