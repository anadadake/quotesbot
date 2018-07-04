# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import urllib.request
import json
import os


class QuotesbotPipeline(object):
    def process_item(self, item, spider):
        return item


class PicPipeline(object):

    # def __init__(self):
    #     self.file = open('xiaohua.json','wb')

    def open_spider(self, spider):
        self.file = open('xiaohua.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        # Process 1: dump into json file
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        # return item


        # Process 2: save pics
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
        req = urllib.request.Request(url=item['pic_url'], headers=headers)
        res = urllib.request.urlopen(req)

        print(item['name'])

        file_name = os.path.join(r'D:\Downloads\1111', item['name'] + '.jpg')
        with open(file_name, 'wb') as fp:
            fp.write(res.read())

        return item


class QuotesPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item
