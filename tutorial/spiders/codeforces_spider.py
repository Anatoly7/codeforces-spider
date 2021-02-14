# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 02:55:11 2021

@author: Anato
"""

from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

main_dir = str(source_dir.parent)
info_dir = main_dir + '/info/'

def open_info(file_name, mode):
    return open(info_dir + file_name + '.txt', mode)


import scrapy
from urllib.parse import urljoin

class MySpider(scrapy.Spider):
    name = "cfspider"
    allowed_domains = ["codeforces.com"]
    visited_urls = []
    d = {}
    
    def start_requests(self):                   
        with open_info('to_check', 'r') as f:
            self.d = dict.fromkeys([el for el in f.read().split()], 1)

        fs = open_info('result', 'w')
        fs.close()

        url = ""
        with open_info('s_url', 'r') as f:
            url = f.read() + '/standings/page/1'
            #self.logger.info(url)
        yield scrapy.Request(url = url, callback = self.parse)
        
    def parse(self, response):
        a = response.xpath('//tr[@participantid]/td[2]/a/text()').extract()
        
        #with open('debug.txt', 'a') as f:
        #   for el in a:
        #       f.write(el + '\n')
                
        with open_info('result', 'a') as f:
            for el in a:
                if el in self.d:
                    f.write(el + '\n')
        
        next_pages = response.xpath('//a[contains(@href,"standings/page")]/@href').extract()
        
        for next_page in next_pages:
            url = urljoin(response.url + '/', next_page)
            if url not in self.visited_urls:
                self.visited_urls.append(url)
                yield response.follow(url, callback = self.parse)
        
        
