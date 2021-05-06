from src.scrape import Scraper
import requests
import json


class ScrapeAliexpress(Scraper):
    @staticmethod
    def get_api(item):
        url = "https://magic-aliexpress1.p.rapidapi.com/api/products/search"

        querystring = {"name": item,
                       "page": "1"}  # ,"minSalePrice":"5","shipToCountry":"FR","sort":"NEWEST_DESC","page":"1","maxSalePrice":"1000000","shipFromCountry":"CN","fastDelivery":"true"

        headers = {
            'x-rapidapi-key': "709a585a71msh9ea746b2aeae379p13ffb0jsn25aff23b5005",
            'x-rapidapi-host': "magic-aliexpress1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        return json.loads(str(response.text))

    @staticmethod
    def extract_record(response):
        records = []

        for item in response['docs']:
            title = item['product_title']
            price = round(item['app_sale_price'], 2)
            currency = item['app_sale_price_currency']
            url = item['product_detail_url']

            try:
                rating_val = item['evaluate_rate']
                rating = str(rating_val) + ' out of 5 stars'
            except:
                rating_val = 0
                rating = 'no rating'

            result = {
                'title': title,
                'price': price,
                'currency': currency,
                'rating': rating,
                'url': url
            }

            records.append(result)

        return records

    def scrape(self, search_item):
        api = self.get_api(search_item)
        product = self.extract_record(api)
        return product
