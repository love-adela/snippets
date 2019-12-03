import Scrapy 

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = ['http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09&year=2008&month=1'
                'http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=09&year=2008&month=2',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
