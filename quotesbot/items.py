# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesbotItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_name = scrapy.Field()
    author_homepage_url = scrapy.Field()
    summary = scrapy.Field()

    # pass


class XiaohuaItem(scrapy.Item):
    name = scrapy.Field()
    pic_url = scrapy.Field()
    home_page_url = scrapy.Field()

class MatplotlibExampleSrcItem(scrapy.Item):
    example_name = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()