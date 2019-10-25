# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BillboardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field
    date = scrapy.Field()
    date_str = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    commentsUrl = scrapy.Field()

    pass

class FuseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field
    date = scrapy.Field()
    date_str = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    commentsUrl = scrapy.Field()

    pass

class LoudwireItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field
    date = scrapy.Field()
    date_str = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    commentsUrl = scrapy.Field()

    pass
