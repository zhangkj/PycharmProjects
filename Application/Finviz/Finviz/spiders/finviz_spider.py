import  sys
sys.path.append("F:\mystuff\PycharmProjects\Application\Finviz")
from scrapy import Spider
from scrapy.selector import Selector
from Finviz.items import FinvizItem

class FinvizSpider(Spider):
        name = "finviz"
        allowed_domains = ["finviz.com"]
        start_urls = [
            "http://www.finviz.com/screener.ashx?v=151&r=1",
            "http://www.finviz.com/screener.ashx?v=151&r=1000",
        ]

        def parse(self, response):
            questions = Selector(response).xpath('//table[@bgcolor="#d3d3d3"]/tr[@valign="top"]')

            for question in questions:
                item = FinvizItem()
                item['Ticker'] = question.xpath(
                    'td[2]/a/text()').extract()[0]
                item['Company'] = question.xpath(
                    'td[3]/a/text()').extract()[0]
                item['Sector'] = question.xpath(
                    'td[4]/a/text()').extract()[0]
                item['Industry'] = question.xpath(
                    'td[5]/a/text()').extract()[0]
                item['ATR'] = question.xpath(
                    'td[11]/a/text()').extract()[0]
                item['AvgVolume'] = question.xpath(
                    'td[11]/a/text()').extract()[0]
                item['Price'] = question.xpath(
                    'td[11]/a/text()').extract()[0]
                item['Change'] = question.xpath(
                    'td[11]/a/text()').extract()[0]
                item['Volume'] = question.xpath(
                    'td[11]/a/text()').extract()[0]
                yield item