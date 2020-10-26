import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

# dict of all links except 'more' category
sites = {
    'wasser': 'https://www.durstexpress.de/dresden/mineralwasser?product_list_limit=all',
    'saft': 'https://www.durstexpress.de/dresden/saft?product_list_limit=all',
    'limo': 'https://www.durstexpress.de/dresden/limonaden-schorlen?product_list_limit=all',
    'bier': 'https://www.durstexpress.de/dresden/bier?product_list_limit=all',
    'wein': 'https://www.durstexpress.de/dresden/wein?product_list_limit=all',
    'spirituosen': 'https://www.durstexpress.de/dresden/spirituosen?product_list_limit=all'
}

articles = {
    
}

def searchCategory():   
    try:        
        for key in sites:
            url = sites[key]
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            getItemID(soup)
    except requests.exceptions.ConnectionError:
        pass  

def getItemID(soup):
    for item in soup.find_all('div', {'class' : 'product details product-item-details'}):
        item_id = item.find('div', {'class': 'price-box price-final_price'}).get('data-product-id')
        if isSpecial(soup, item_id) == True:
            getDetails(soup, item_id)
        else:
            pass    

def isSpecial(soup, itemid):
    item = soup.find('div', {'data-product-id' : itemid})
    price_label = item.find('span', {'class' : 'price-container price-final_price tax weee'}).get_text()
    if "Angebotspreis" in price_label:
        return True
    else:
        return False    

def getDetails(soup, item_id):
    for item in soup.find_all('div', {'class' : 'product details product-item-details'}):
        current_item_id = item.find('div', {'class' : 'price-box price-final_price'}).get('data-product-id')
        marke = item.find('a', {'class': 'product-item-link'}).get('title')
        price = item.find('span', {'class' : 'price'}).get_text()
        if current_item_id == item_id:
            articles[marke] = price
  
def getArticles():
    return articles    