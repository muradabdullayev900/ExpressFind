from bs4 import BeautifulSoup
from src.scrape import Scraper
from src.driver import Driver

tapaz_driver = Driver(True)


class ScrapeTapaz(Scraper):
    def __init__(self):
        self.driver = tapaz_driver.get_driver()

    @staticmethod
    def get_url(search_term):
        search_term = search_term.replace(' ', '+')
        template = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={search_term}&q%5Bregion_id%5D='
        return template

    @staticmethod
    def extract_record(item):
        try:
            atag = item.a
            title = item.find('div', {'class': 'products-name'}).text.strip()
            url = 'https://tap.az' + atag.get('href')[:-9]
        except AttributeError:
            title = 'No title provided'
            url = ''

        try:
            price = item.find('div', {'class': 'products-price'}).text.strip()
            price = float(price[:-3].replace(',', '').replace(' ', ''))
            currency = 'AZN'
        except AttributeError:
            price = 0
            currency = ''

        result = {
            'title': title,
            'price': price,
            'currency': currency,
            'url': url,
            'source': 'tap.az'
        }

        return result

    def scrape(self, search_item):

        records = []

        url = self.get_url(search_item)

        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div', {'class': "products-i rounded"}) + soup.find_all('div', {
            'class': "products-i rounded bumped products-shop"}) + soup.find_all('div',
                                                                                 {'class': "products-i rounded bumped"})

        for item in results:
            if len(records) == 20:
                break
            else:
                record = self.extract_record(item)
                if record:
                    records.append(record)


        return records

