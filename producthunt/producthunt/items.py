# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from w3lib.html import remove_tags
from itemloaders.processors import TakeFirst , MapCompose


class ProducthuntItem(scrapy.Item):
    # define the fields for your item here like:
     name = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
     free = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
     genre = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor=TakeFirst())
    
