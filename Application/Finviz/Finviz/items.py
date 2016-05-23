# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class FinvizItem(Item):
    Ticker = Field()
    Company = Field()
    Sector = Field()
    Industry = Field()
    ATR = Field()
    AvgVolume = Field()
    Price = Field()
    Change = Field()
    Volume = Field()

