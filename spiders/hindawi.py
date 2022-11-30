import scrapy
from scrapy.spiders import CrawlSpider

class HindawiSpider(CrawlSpider):
    name = 'hindawi'
    allowed_domains = ['www.hindawi.org']
    start_urls = ['https://www.hindawi.org/books/categories/travel.literature/']