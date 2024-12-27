import scrapy
import mysql.connector
import requests
from pathlib import Path
from scrapy import selector, Selector


class ProductDetailsSpider(scrapy.Spider):
    name = "product"
    domain = ["https://www.purplle.com/"]
    start_url=["https://www.purplle.com/page/1/",
               "https://www.purplle.com/page/2/"]

    def __init__(self):
        print("ok")

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"product-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")

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
name=select.xpath('//div[@class="product-title fs-7 text-start text-black fw-normal"]/text()').get()
price=select.xpath('//span[@class="text-black fw-bolder fs-6 f18i"]/text()').get()
defordicount=select.xpath('//span[@class="fw-bold float-start position-relative clearfix w-100 text-center ng-star-inserted"]/text()').get()
rateing=select.xpath('//span[@class="star-rating bg-success rounded-4 fs-8 text-white fw-bold ng-star-inserted"]/text()').get()
userreview=select.xpath('text-black-50 ms-1 fs-8 ng-star-inserted').get()



print(price)
print(name)
# p.parse(response)