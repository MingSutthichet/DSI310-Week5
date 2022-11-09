import scrapy

class QuotesSpider(scrapy.Spider):
    name = "bbc_edu"
    start_urls = [
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=1',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=2',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=3',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=4',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=5',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=6',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=7',
        'https://www.bbc.com/thai/topics/c06gqj3g7pqt?page=8',
    ]

    def parse(self, response):
        for quote in response.css('div.promo-text'):
            yield {
                'title': quote.css('a::text').get(),
                'date': quote.css('time::text').get(),
            }

        next_page = response.css('span.ALL a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
