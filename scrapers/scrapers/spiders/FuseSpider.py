from datetime import datetime as dt
import scrapy
from scrapers.items import FuseItem

class PostSpider(scrapy.Spider):
        name = 'fuse'

        allowed_domains = ['fuse.tv']

        urls = [
                "https://www.fuse.tv/latest#read" # selecionando a url específica que contém as notícias do site
                ]

        def parse(self, response):
            news = Selector(response).xpath('//div[@class="imagetitle"]/h1') # modificando o XPath do site para conseguir todas as notícias

            for iterator in news:

                item = FuseItem()
                item['title'] = iterator.xpath('a[@class="imagetitle"]/text()').extract()[0] ''' TODO: função nece                                                                                                                                                           não se sabe até então como se passar                                                                                                                                        o xpath da forma correta '''

                                                                                                                                                                                             yield item
