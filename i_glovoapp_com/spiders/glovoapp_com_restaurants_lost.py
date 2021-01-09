import scrapy
from scrapy.crawler import CrawlerProcess
import re

from iii_glovoapp_com.i_glovoapp_com.spiders.locators import Locators
from iii_glovoapp_com.i_glovoapp_com.items import GlovoappComRestaurantsItem


class GlovoappComRestaurantsLostSpider(scrapy.Spider):
    name = 'glovoapp_com_restaurants_lost'
    start_urls = ['https://glovoapp.com/es/seg/#']

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': f"../../iii_results/{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
        'FEED_EXPORT_FIELDS': [
            'city',
            'city_restaurants_url',
            'restaurant_name',
            'restaurant_url',
        ]
    }

    def parse(self, response, **kwargs):
        codes = [
            # 'SDQ',
            # 'BUC',
            # 'NBO',
            # 'PAN',
            # 'VAL',
            # 'KHA',
            # 'LVI',
            # 'TIM',
            # 'IAS',
            # 'TIM',
            'KIE',
            # '',
            # '',
            # '',
            # '',
        ]

        for code in codes:
            url = f'https://glovoapp.com/es/{code}/category/RESTAURANT/'
            yield scrapy.Request(url=url, callback=self.parse_city_restaurants)

    @staticmethod
    def parse_city_restaurants(response):
        items = GlovoappComRestaurantsItem()

        city = response.xpath(Locators.CITY).get()
        if city is not None:
            items['city'] = city
            city_restaurants_url = response.url
            items['city_restaurants_url'] = city_restaurants_url

            yield items

            restaurants = response.xpath(Locators.RESTAURANTS)
            for restaurant in restaurants:
                restaurant_name = restaurant.xpath(Locators.RESTAURANT_NAME).get()
                restaurant_url = restaurant.xpath(Locators.RESTAURANT_URL).get()

                items['city'] = None
                items['city_restaurants_url'] = None
                items['restaurant_name'] = restaurant_name
                items['restaurant_url'] = f'https://glovoapp{restaurant_url}'

                yield items
        else:
            pass


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(GlovoappComRestaurantsLostSpider)
    process.start()
