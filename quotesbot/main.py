from scrapy import cmdline

if __name__ == '__main__':

    # example test
    # cmdline.execute('scrapy crawl toscrape-css -o toscrape-css.json'.split())

    #CSDN blog test
    # cmdline.execute('scrapy crawl csdn_blog -o test.json'.split())

    #美剧网
    #cmdline.execute('scrapy crawl meijutt_new_100 -o meiju.csv'.split())

    #校花网
    # cmdline.execute('scrapy crawl xiaohua_spider -o xiaohua.csv '.split())

    #爬取http://quotes.toscrape.com/， 带换页
    cmdline.execute('scrapy crawl quoters_spider -o quoters_spider.csv'.split())
