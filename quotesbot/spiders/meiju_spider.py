# -*- coding: utf-8 -*-
import scrapy
import urllib


# 获取【美剧天堂】前100.http://www.meijutt.com/new100.html
class MeijuttNew100Spider(scrapy.Spider):
    name = "meijutt_new_100"
    start_urls = [
        'http://www.meijutt.com/new100.html'
    ]

    def parse(self, response):

        drama_names=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        # articles = response.css('div#article_list div.article_item')
        for drama_name in drama_names:
            title = drama_name.xpath('./h5/a/@title').extract_first().strip()
            # link = self.base_url + article.css('div.article_title a::attr(href)').extract_first().strip()
            yield {'title': title}

        # pages = response.css('div#papelist')
        # next_page_url = pages.css('a').re_first('<a href=\"(.*)\">下一页')
        # if next_page_url is not None:
        #     yield scrapy.Request(urllib.parse.urljoin(self.base_url, next_page_url))
