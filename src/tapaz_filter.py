from src.displayer import Displayer
from src.tapaz_scrape import ScrapeTapaz


class TapazFilter(Displayer):
    def __init__(self):
        self.tapaz_scraper = ScrapeTapaz()

    def convert_cur(self, record, currency):
        if currency == 'usd':
            for price in record:
                price['price'] *= 0.59
                price['price'] = round(price['price'], 2)
                price['currency'] = 'USD'
        return record

    def minMaxFilter(self, record, min_price, max_price):
        if min_price or max_price:
            record = filter(lambda x: min_price < x['price'] < max_price, record)
        return record

    def sorter(self, record, sort):
        record = sorted(record, key=lambda k: k['price'], reverse=(sort != 'ascending'))
        return record

    def Filter(self, record, sort, currency, min_price, max_price):
        records = self.tapaz_scraper.scrape(record)
        records = self.convert_cur(records, currency)
        records = self.sorter(records, sort)
        records = self.minMaxFilter(records, min_price, max_price)
        return records
