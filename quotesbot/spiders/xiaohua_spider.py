import scrapy
from quotesbot.items import XiaohuaItem

# 爬取校花网的图片
class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua_spider'
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        # print(self.base_url)
        for pic_item_t in response.xpath('//div[@class="item_t"]'):
            xiaohua = XiaohuaItem()

            xiaohua['name'] = pic_item_t.xpath('./div[@class="img"]/span[@class="price"]/text()').extract_first()
            xiaohua['home_page_url'] = pic_item_t.xpath('./div[@class="img"]/a/@href').extract_first()
            xiaohua['pic_url'] = 'http://www.xiaohuar.com' + pic_item_t.xpath('./div[@class="img"]/a/img/@src').extract_first()

            yield xiaohua

            # yield {
            #     'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
            #     'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
            #     'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract()
            # }

        # next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))
