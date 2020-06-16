import scrapy
class zapposSpider(scrapy.Spider):
    name = 'zappos'
    start_urls = ['https://www.zappos.com/men-running-shoes']
    alloewd_domains = ['www.zappos.com']

    custom_settings = {
        'FEED_URI': 'tmp/zappos.csv'
    }
    def parse(self, response):
        for product in response.css('article'):
            yield {
                "name": product.css("p[itemprop = 'name']::text").extract_first()
            }