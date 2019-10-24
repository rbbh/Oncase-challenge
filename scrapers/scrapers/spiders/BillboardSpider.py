
from datetime import datetime as dt
import scrapy
from billboard.items import BillboardItem

class PostSpider(scrapy.Spider):
    name = 'billboard'

    allowed_domains = ['billboard.com']

    urls = [
                "https://www.billboard.com/news"
           ]

    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)
