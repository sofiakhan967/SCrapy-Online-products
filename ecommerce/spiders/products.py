import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75.html']

    def parse(self, response):
        for product in response.xpath('//div[@class="p_box_wrapper"]'):

            yield{

                    'title':product.xpath('.//div/a[@class="p_box_title"]/text()').get(),
                    'url':product.xpath('.//div/a[@class="p_box_title"]/@href').get(),
                    'price':product.xpath('.//div/div[@class="p_box_price cf"]/text()').get()
            }
        page = response.xpath('//a[@class="nextPage"]/@href').get()
        if page:
            yield scrapy.Request(url=page,callback=self.parse)
        

