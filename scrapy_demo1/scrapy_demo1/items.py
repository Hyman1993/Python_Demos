# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemo1Item(scrapy.Item):
    # define the fields for your item here like:
    # 老师姓名
    date = scrapy.Field()
    # 老师职称
    title = scrapy.Field()
    # 老师信息
    url = scrapy.Field()
    #pass

