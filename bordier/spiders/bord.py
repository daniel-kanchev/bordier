import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from bordier.items import Article


class BordSpider(scrapy.Spider):
    name = 'bord'
    allowed_domains = ['bordier.com']
    start_urls = ['https://www.bordier.com/en/bordier-group-latest-news/']

    def parse(self, response):
        articles = response.xpath('//a[@data-av-masonry-item]')
        for article in articles:
            print('yeet')
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            link = article.xpath('.//@href').get()
            title = article.xpath('.//h3/text()').get()
            category = article.xpath('.//spam/text()').get()
            date = article.xpath('.//span/text()').get()

            item.add_value('title', title)
            item.add_value('date', date)
            item.add_value('category', category)
            item.add_value('link', link)

            yield item.load_item()
