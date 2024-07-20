import scrapy

class MySpider(scrapy.Spider):
    name = 'scrape_multiple_website_spider'
    start_urls = ['https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&fm=neo%2Fmerchandising&iid=M_8b3b3f65-7ceb-4375-912c-d2bcdde87c58_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_13_L1_view-all&cid=34WHNYFH5V2Y&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkFzdXMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&otracker=clp_metro_expandable_5_7.metroExpandable.METRO_EXPANDABLE_Asus_laptops-store_PUCYCBKIVJML_wp6&fm=neo%2Fmerchandising&iid=M_2694736b-2f0f-49aa-9c24-14d42accf9c6_7.PUCYCBKIVJML&ppt=hp&ppn=homepage&ssid=eobtr0deb40000001717133028019&sort=price_asc']

    def parse(self, response):
        self.log(f'Scraped URL: {response.url}')

        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
