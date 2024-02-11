import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["apple.com"]
    start_urls = ["https://apple.com"]

    def parse(self, response):
        pass
