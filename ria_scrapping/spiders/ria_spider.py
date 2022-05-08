import scrapy


class RiaSpider(scrapy.Spider):
    name = 'ria'
    allowed_domains = ['ria.ru']
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'DOWNLOAD_DELAY': 5,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5,
        'AUTOTHROTTLE_DEBUG': True,
        'CONCURRENT_REQUESTS': 1
    }

    start_urls = [
        'https://ria.ru/search/?query=&offset=20&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=40&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=60&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=80&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=100&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=120&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=140&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=160&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=180&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=200&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=220&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=240&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=260&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=280&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=300&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=320&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=340&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=360&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=380&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=400&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=420&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=440&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=460&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=480&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=500&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=520&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=540&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=560&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=580&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=600&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=620&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=640&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=660&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=680&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=700&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=720&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=740&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=760&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=780&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=800&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=820&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=840&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=860&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=880&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=900&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=920&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=940&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=960&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=980&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08',
        'https://ria.ru/search/?query=&offset=1000&interval=&date_from=2022-01'
        '-01&date_to=2022-05-08'
    ]

    def parse(self, response):
        print('print:', response.url)
        for article in response.css('div.list-item a::attr(href)'):
            yield response.follow(article, callback=self.parse_news)

    def parse_news(self, response):
        yield {
            'title': response.css('div.article__title::text').get(),
            'alt_title': response.css('h1.article__title::text').get(),
            'date': response.css('div.article__info-date a::text').get(),
            'text': response.css('div.article__text::text').getall()
        }
