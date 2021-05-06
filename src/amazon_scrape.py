from bs4 import BeautifulSoup
from src.scrape import Scraper
from src.driver import amazon_driver


class ScrapeAmazon(Scraper):
    def __init__(self):
        self.driver = amazon_driver.get_driver()

    @staticmethod
    def get_url(search_term):
        search_term = search_term.replace(' ', '+')
        template = f'https://www.amazon.com/s?k={search_term}&crid=2LVUHRLNH01PN&sprefix=ultrawide%2Caps%2C354&ref=nb_sb_ss_ts-doa-p_1_9'
        template += '&page={}'
        return template

    @staticmethod
    def extract_record(item):
        try:
            atag = item.h2.a
            title = atag.text.strip()
            url = 'https://amazon.com' + atag.get('href')
        except AttributeError:
            title = 'No title provided'
            url = ''

        try:
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
            price = float(price[1:].replace(',', ''))
            currency = 'USD'
        except AttributeError:
            price = 0
            currency = ''
        try:
            rating = item.i.text
        except AttributeError:
            rating = 'no rating'

        result = {
            'title': title,
            'price': price,
            'currency': currency,
            'rating': rating,
            'url': url
        }

        return result

    def scrape(self, search_item):

        records = []

        url = self.get_url(search_item)

        for i in range(1, 10):
            self.driver.get(url.format(i))
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all('div', {'data-component-type': 's-search-result'})
            stop = False
            for item in results:
                if len(records) == 20:
                    stop = True
                record = self.extract_record(item)
                if record['price'] == 0:
                    continue
                else:
                    if record:
                        records.append(record)
            if stop:
                break

        return records

