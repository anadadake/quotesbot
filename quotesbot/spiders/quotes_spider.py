import scrapy
from quotesbot.items import QuotesbotItem

class QuotesSpider(scrapy.Spider):
    """
    ver 1.0.0 simply get author info and store into quoters_spider.csv on 2018-07-03
    ver 1.1.0 add item pipeline to save as json format into file on 2018-07-04
    """
    name = 'quoters_spider'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            summary = quote.xpath('./span[@class="text"]/text()').extract_first()
            author_name = quote.xpath('.//small[@class="author"]/text()').extract_first()
            author_homepage_url = response.urljoin(quote.xpath('.//a[1]/@href').extract_first())

            # print("@@@ " + author_name + " Done.")
            item = QuotesbotItem()
            item["summary"] = summary
            item["author_name"] = author_name
            item["author_homepage_url"] = author_homepage_url

            yield item


            # yield {
            #     'author_name': author_name,
            #     'author_homepage_url': author_homepage_url,
            #     'summary': summary
            # }

        next_url_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url_page is not None:
            yield scrapy.Request(response.urljoin(next_url_page))
