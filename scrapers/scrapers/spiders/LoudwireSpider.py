from datetime import datetime as dt
import scrapy
from scrapers.items import LoudwireItem

class PostSpider(scrapy.Spider):
        name = 'loudwire'

        allowed_domains = ['loudwire.com']

        urls = [
                "https://loudwire.com/category/news/" # selecionando a url específica que contém as notícias do site
                ]

        def parse(self, response):
            news = Selector(response).xpath('//div[@class="content"]') # modificando o XPath do site para conseguir todas as notícias

            for iterator in news:

                item = LoudwireItem()
                item['title'] = iterator.xpath('a[@class="content-title"]/text()').extract()[0] ''' TODO: função nece                                                                                                                                                           não se sabe até então como se passar                                                                                                                                        o xpath da forma correta '''


                 yield item
