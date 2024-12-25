import scrapy
import mysql.connector
import requests
from scrapy import selector, Selector


class ProductDetailsSpider(scrapy.Spider):
    name = "product"
    start_urls = ["https://www.purplle.com/"]

    def __init__(self):
        print("ok")


p=ProductDetailsSpider()


import requests

import requests

headers = {
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'q': 'Lip',
}

response = requests.get('https://www.purplle.com/search', params=params, headers=headers)
print(response)
select=Selector(text=response.text)
text=select.xpath('.//div[@class="product-title fs-7 text-start text-black fw-normal"]/text()').get()
title=select.xpath('.//span[@class="fw-bold float-start position-relative clearfix w-100 text-center ng-star-inserted"]/text()').get()
print(text)
print(title)