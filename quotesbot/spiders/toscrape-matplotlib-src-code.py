# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibExampleSrcItem
class ToScrapeMatplotlibSpider(scrapy.Spider):
    name = "toscrape-matplotlib"
    allowed_domains = ["matplotlib.org"]
    start_urls = [
        'http://matplotlib.org/examples/index.html',
    ]

    def parse(self, response):
        le = LinkExtractor(restrict_css='li.toctree-l2')
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_detail)




    def parse_detail(self,response):
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        name = response.xpath('//h1/text()').extract_first()

        exampleItem = MatplotlibExampleSrcItem()
        exampleItem['example_name']= name
        exampleItem['file_urls']= [url]
        return exampleItem


        # for quote in response.css("div.quote"):
        #     yield {
        #         'text': quote.css("span.text::text").extract_first(),
        #         'author': quote.css("small.author::text").extract_first(),
        #         'tags': quote.css("div.tags > a.tag::text").extract()
        #     }
        #
        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

