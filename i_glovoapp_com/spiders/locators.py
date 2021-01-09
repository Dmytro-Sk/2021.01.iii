class Locators:

    """Page 1"""
    
    # main locators
    RESTAURANT_NAME = './/h3/text()'
    CITY = '//span[@data-test-id="city-picker-current-city"]/text()'
    RESTAURANT_URL = './@href'

    # additional locators
    RESTAURANTS = '//div[@data-test-id="category-store-list"]/a'

    """Page 2"""

    # main locators

    # additional locators
    CITIES = '/html/body/script[2]/text()'
