import scrapy
from scrapy.loader import ItemLoader
from lianjia.items import LianjiaItem
from urllib.parse import urljoin
import re

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia_spider'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://cd.lianjia.com/ershoufang/']
    
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
    }

    def parse(self, response):
        # 解析房源列表
        house_links = response.css('.sellListContent li .title a::attr(href)').getall()
        for link in house_links:
            yield response.follow(link, self.parse_house_detail)
            
        # 分页处理
        next_page = response.css('.page-box .next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_house_detail(self, response):
        loader = ItemLoader(item=LianjiaItem(), response=response)
        
        # 基本信息
        loader.add_css('title', '.title .main::text')
        loader.add_css('price', '.price .total::text')
        loader.add_css('unit_price', '.unitPrice .unitPriceValue::text')
        loader.add_css('community', '.communityName .info::text')
        loader.add_css('district', '.areaName .info a::text')
        loader.add_value('detail_url', response.url)
        
        # 房屋基本信息
        house_info = {}
        for info in response.css('.introContent .content li'):
            key = info.css('span.label::text').get()
            value = info.css('::text').getall()[-1].strip()
            house_info[key] = value
        loader.add_value('basic_info', house_info)
        
        # 交易信息
        transaction_info = {}
        for info in response.css('.transaction .content li'):
            key = info.css('span.label::text').get()
            value = info.css('span:nth-child(2)::text').get()
            transaction_info[key] = value
        loader.add_value('transaction_info', transaction_info)
        
        # 位置信息
        position_info = response.css('.areaName .info a::text').getall()
        if len(position_info) >= 2:
            loader.add_value('location', ' '.join(position_info[:2]))
        
        yield loader.load_item()