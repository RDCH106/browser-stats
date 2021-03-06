# -*- coding: utf-8 -*-
import scrapy


class BrowserStatsSpider(scrapy.Spider):
    name = 'browser-stats'
    allowed_domains = ['https://www.w3schools.com/Browsers/default.asp']
    start_urls = ['https://www.w3schools.com/Browsers/default.asp']

    def parse(self, response):
        first_table = 0
        for table in response.css('table'):
            if first_table == 0:
                yield{
                    'name': 'Browsers Stats ' + table.css("th::text").extract_first(),
                    'header': [table.css("th::text").extract_first()] + table.css("th a::text").extract(),
                    'data': table.css("td::text").extract()
                }
                first_table = 1
            else:
                yield{
                    'name': 'Browsers Stats ' + table.css("th::text").extract_first(),
                    'header': table.css("th::text").extract(),
                    'data': table.css("td::text").extract()
                }
