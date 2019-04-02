# -*- coding: utf-8 -*-
import scrapy
from itbooks.items import ItbooksItem

class AlliteSpiderSpider(scrapy.Spider):
    name = 'allite_spider'
    allowed_domains = ['http://www.allitebooks.com/']
    start_urls = ['http://www.allitebooks.com/?s=python']

    def parse(self, response):
        for sel in response.xpath('//article/div[1]'):
            url = sel.xpath('a/@href').extract_first()
            yield scrapy.Request(url, callback=self.parse_download, dont_filter=True)
        next_link = response.xpath('//*[@id="main-content"]/div/div/span[@class="current"]/text()').extract()
        print(type(next_link), next_link)
        next_link = int(next_link[0])+1
        if next_link:
            yield scrapy.Request('http://www.allitebooks.com/page/'+str(next_link)+'/?s=python',
            callback=self.parse, dont_filter=True)

    # def parse_detail(self, response):
    #     for sel in response.xpath('//article/div[1]'):
    #         url = sel.xpath('a/@href').extract_first()
    #         yield scrapy.Request(url, callback=self.parse_download, dont_filter=True)

    def parse_download(self, response):
        item = ItbooksItem()
        item['file_urls'] = response.xpath('//*[@id="main-content"]/div/article/footer/div/span[1]/a/@href').extract()
        yield item
