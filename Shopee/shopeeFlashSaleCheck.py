#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

sale_url = "https://shopee.vn/flash_sale?categoryId=13"

if __name__=="__main__":
    # html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    html = requests.get(sale_url)
    soup = BeautifulSoup(html.text, "html.parser")
    # bsObj = BeautifulSoup(html.read())
    # print(bsObj.h1)

    
