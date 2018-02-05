# -*- coding: utf-8 -*-
import scrapy


class Sex8Spider(scrapy.Spider):
    name = 'sex8'
    allowed_domains = ['sex8.xin']
    start_urls = ['http://sex8.xin/']

    def parse(self, response):
        for sel in response.xpath('//div/input'):
			print sel.xpath('@type').extract()
