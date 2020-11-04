# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliListScrItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    name = scrapy.Field()
    pic = scrapy.Field()
    url = scrapy.Field()
    aid = scrapy.Field()
    bv = scrapy.Field()
    view = scrapy.Field()
    up = scrapy.Field()
    upId = scrapy.Field()
    date = scrapy.Field()
    type = scrapy.Field()


