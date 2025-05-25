import requests
from bs4 import BeautifulSoup

def scrape_items(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    items = []
    for product in soup.find_all('div', class_='product'):  # Adjust class name based on site
        name = product.find('h2').text
        image_url = product.find('img')['src']
        items.append({'name': name, 'image_url': image_url})
    
    return items