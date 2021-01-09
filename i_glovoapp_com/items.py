# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GlovoappComRestaurantsItem(scrapy.Item):
    code = scrapy.Field()
    city = scrapy.Field()
    city_restaurants_url = scrapy.Field()
    restaurant_name = scrapy.Field()
    restaurant_url = scrapy.Field()
