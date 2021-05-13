from src.displayer import Displayer
from src.amazon_scrape import ScrapeAmazon

amazon_scraper = ScrapeAmazon()

class AmazonFilter(Displayer):
    def __init__(self):
        self.amazon_scraper = amazon_scraper

    def convert_cur(self, record, currency):
        if currency == 'azn':
            for price in record:
                price['price'] *= 1.70
                price['price'] = round(price['price'], 2)
                price['currency'] = 'AZN'
        return record

    def minMaxFilter(self, record, min_price, max_price):
        if min_price or max_price:
            record = filter(lambda x: min_price < x['price'] < max_price, record)
        return record

    def sorter(self, record, sort):
        if sort == 'ascending':
            record = sorted(record, key=lambda k: k['price'], reverse=False)
        elif sort == 'descending':
            record = sorted(record, key=lambda k: k['price'], reverse=True)
        return record

    def Filter(self, record, sort, currency, min_price, max_price):
        records = self.amazon_scraper.scrape(record)
        records = self.convert_cur(records, currency)
        records = self.sorter(records, sort)
        records = self.minMaxFilter(records, min_price, max_price)
        return records
