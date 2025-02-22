# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UandesscraperItem(scrapy.Item):
    # define the fields for your item here like:
    news = scrapy.Field()
    href = scrapy.Field()
    course = scrapy.Field()
    newsContent = scrapy.Field()
    courseName = scrapy.Field()
    newsDate = scrapy.Field()
    newsTitle = scrapy.Field()
    table = scrapy.Field()
    openActivityTitle = scrapy.Field()
    openActivityDate = scrapy.Field()
    user = scrapy.Field()
    uandesNewsTitles = scrapy.Field()
    uandesNewsDates = scrapy.Field()

    pass
