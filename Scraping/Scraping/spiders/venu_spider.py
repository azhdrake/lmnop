import scrapy
from scrapy.crawler import CrawlerProcess
import re
#from ..items import Event
all_events = []

class Event(scrapy.Item):
    name = scrapy.Field()
    artist = scrapy.Field()
    venue = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()
    ages = scrapy.Field()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://first-avenue.com/calendar',
    ]

    def parse(self, response):
        page = response.css('body').get()
        

        matches = re.findall("\"field-item even\"><a href=\"(/event[^\"]+)\">([^<]+)[\s\S]+?a href=\"/venue[^\"]+\">([^<]+)[\s\S]+?\"date-display-single\">([^<]+)[\s\S]+?even\">([^<]+)", page)
        
        for match in matches:
            event = Event(url = 'https://first-avenue.com' + match[0], name = match[1], venue = match[2], time = match[3], ages = match[4])
            all_events.append(event)

        """next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)"""

process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()