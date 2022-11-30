# Models for scraped items

import scrapy

class ZipfilesItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field
    original_file_name = scrapy.Field()