# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LianjiaItem(scrapy.Item):
    # 确保每个字段都单独声明
    title = scrapy.Field()
    price = scrapy.Field()
    unit_price = scrapy.Field()  # 这是关键字段
    location = scrapy.Field()
    detail_url = scrapy.Field()
    basic_info = scrapy.Field()
    transaction_info = scrapy.Field()
    community = scrapy.Field()
    district = scrapy.Field()
    
    # 可选：添加__repr__方法方便调试
    def __repr__(self):
        return f"<LianjiaItem: {self.get('title', '')}>"