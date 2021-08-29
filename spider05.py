import scrapy
from scrapy import Selector, Item, Field
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
import json
import pandas as pd
from os.path import exists


"""class Frase(Item):
    id = Field()
    frase = Field()
"""

class TestSpider(Spider):
    rate = 1

    def __init__(self):
        # self.download_delay = 1 / float(self.rate)
        self.download_delay = 1

    name = 'spider05'
    item_count = 0
    allowed_domains = ['parascrapear.com']
    start_urls = ['https://parascrapear.com/']

    def parse(self, response):
        print("------------------------------------------------")
        print('Parseando ' + response.url)
        list = []
        items = response.selector.css('body > blockquote')

        next_page = response.selector.css('body > div:nth-child(23) > a.next::attr(href)').get()
        #next_page = response.selector.css('body > div:nth-child(23) > a.next').attrib['href']
        if next_page is not None:
            print("next_page")
            print(next_page)
            yield response.follow(next_page,callback=self.parse)

        for item in items:
            frase = item.css('p q::text').get()
            list.append(frase)

        file_exists = exists("file.xlsx")
        if file_exists:
            df = pd.read_excel('file.xlsx', sheet_name='Sheet1', dtype=str)
        else:
            df = pd.DataFrame()
        data = {'frase': list,
                'estado': None,
                }
        dfNew = pd.DataFrame(data)
        print(dfNew)
        df = df.append(dfNew)
        df.to_excel("file.xlsx", merge_cells=False, index=False)
        return data
