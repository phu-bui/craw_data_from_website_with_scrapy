import scrapy

class thegioididongSpider(scrapy.Spider):
    name = 'thegioididong'
    allowed_domains = ['www.thegioididong.com']
    start_urls = ['https://www.thegioididong.com/dtdd']

    custom_settings = {
        'FEED_URI': 'tmp/didong.csv'
    }
    def parse(self, response):
        for product in response.css('li'):
            yield {
                "name" : product.css("a h3::text").extract_first(),
                "price": product.css("a div[class = 'price'] strong::text").extract_first(),
                "evaluate": product.css("a div[class = 'ratingresult'] span::text").extract_first(),
                "discount": product.css("a label[class = 'discount']::text").extract_first(),
                "img_url": product.css("a img::attr('src')").extract_first()
            }

        next_url_path = response.css(
            "a[class = 'viewmore']::attr('href')"
        ).extract_first()
        if next_url_path:
            yield scrapy.Request(
                response.urljoin(next_url_path),
                callback=self.parse
            )