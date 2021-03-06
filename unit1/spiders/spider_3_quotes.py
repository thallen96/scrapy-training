import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        quotes = []
        for quote in response.css('div.quote'):
            quotes.append({
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            })
        # spider_4_quotes.py shows this same spider, but it generates
        # the items individually instead of returning all of them in list
        return quotes
