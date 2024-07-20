import scrapy

class MagicpinSpider(scrapy.Spider):
    name = 'magicpin'
    start_urls = ['https://magicpin.in/New-Delhi/Paharganj/Restaurant/Eatfit/store/61a193/delivery/']

    def parse(self, response):
        for menu_item in response.css(
                '.menu-item-selector'):
            yield {
                'name': menu_item.css('.item-name-selector::text').get(),
                'price': menu_item.css('.item-price-selector::text').get(),
            }