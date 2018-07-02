from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute('scrapy crawl toscrape-css -o toscrape-css.json'.split())
    # cmdline.execute('scrapy crawl csdn_blog -o test.json'.split())