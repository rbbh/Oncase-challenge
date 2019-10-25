
from datetime import datetime as dt
import scrapy
from scrapers.items import BillboardItem

class PostSpider(scrapy.Spider):
    name = 'billboard'

    allowed_domains = ['billboard.com']

    urls = [
                "https://www.billboard.com/news" # selecionando a url específica que contém as notícias do site
           ]

    def parse(self, response):
        news = Selector(response).xpath('//div[@class="content-container"]/h3') # modificando o XPath do site para conseguir todas as notícias

        for iterator in news: 

            item = BillboardItem()
            item['title'] = iterator.xpath('a[@class="content-title"]/text()').extract()[0] ''' TODO: função necessita reparos. 
                                                                                                      não se sabe até então como se passar
                                                                                                      o xpath da forma correta '''
            
            yield item




