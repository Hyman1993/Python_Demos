#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

import scrapy
from scrapy_demo1.items import ScrapyDemo1Item

class SpiderDemo1Spider(scrapy.Spider):
    # 爬虫名，启动爬虫时需要的参数*必需）
    name = "spider_demo1"
    # 爬取域范围，允许爬虫在这个域名下进行爬取（可选）
    allowed_domains = ["itcast.cn"]
    # qishiurl列表，爬虫执行后第一批请求，将从这个列表里获取
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        node_list = response.xpath("//div[@class='li_txt']")

        # 用来存储所有的item字段的
        #items = []
        for node in node_list:
            # 创建item字段对象，用来存储信息
            item = ScrapyDemo1Item()
            # .extract() 将xpath对象转换为 Unicode字符串
            name = node.xpath("./h3/text()").extract()
            title = node.xpath("./h4/text()").extract()
            info = node.xpath("./p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            # 返回提取到的每个item数据，给管道文件处理，同时还回回来继续执行后面的代码
            yield item
            #return item
            #return scrapy.Request(url)
            #items.append(item)

       # yield items


