import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import re

from iii_glovoapp_com.i_glovoapp_com.spiders.locators import Locators
from iii_glovoapp_com.i_glovoapp_com.items import GlovoappComRestaurantsItem


class GlovoappComRestaurantsSpider(scrapy.Spider):
    name = 'glovoapp_com_restaurants'
    start_urls = ['https://glovoapp.com/es/val/category/RESTAURANT/']

    # custom_settings = {
    #     'ITEM_PIPELINES': {
    #         'iii_glovoapp_com.i_glovoapp_com.pipelines.GlovoappComRestaurantsPipeline': 300
    #     },
    #     'FEED_EXPORT_BATCH_ITEM_COUNT': 100,
    #     'FEED_FORMAT': 'csv',
    #     'FEED_URI': f"../../iii_results/%(batch_id)02d-{'_'.join(re.findall(r'[A-Z][^A-Z]*', __qualname__)[:-1]).lower()}.csv",
    #     'FEED_EXPORT_FIELDS': [
    #         'restaurant_name',
    #         'city',
    #         'link',
    #     ]
    # }

    def parse(self, response, **kwargs):
        items = GlovoappComRestaurantsItem()

        restaurant_name = response.xpath(Locators.RESTAURANT_NAME).get()
        city = response.xpath(Locators.CITY).get()
        link = response.xpath(Locators.LINK).get()

        items['restaurant_name'] = restaurant_name
        items['city'] = city
        items['link'] = link

        yield items


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(GlovoappComRestaurantsSpider)
    process.start()
