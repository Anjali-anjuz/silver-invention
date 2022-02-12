# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataExtractionItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Job_title = scrapy.Field()
    Image_url = scrapy.Field()
    Address =scrapy.Field()
    Contact_details = scrapy.Field()
    Social_accounts = scrapy.Field()
    Offices = scrapy.Field()
    Languages = scrapy.Field()
    Description = scrapy.Field()
