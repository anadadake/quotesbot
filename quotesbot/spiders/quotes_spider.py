import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quoters_spider'
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            summary = quote.xpath('./span[@class="text"]/text()').extract_first()
            author_name = quote.xpath('.//small[@class="author"]/text()').extract_first()
            author_homepage_url = response.urljoin(quote.xpath('.//a[1]/@href').extract_first())

            print("@@@ " + author_name + " Done.")

            yield {
                'summary': summary,
                'author_name': author_name,
                'author_homepage_url': author_homepage_url
            }

        next_url_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_url_page is not None:
            yield scrapy.Request(response.urljoin(next_url_page))
