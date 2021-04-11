import csv
from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_term):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term)
    url += '&page{}'
    return url


def extract_record(item):
    atag = item.h2.a
    decription = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return

    try:
        rating = item.i.text
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        rating = ''
        review_count = ''

    result = (decription, price, rating, review_count, url)

    return result


def main(search_item):
    driver = webdriver.Chrome('D:/Compressed/chromedriver.exe')

    records = []
    records_api = []

    url = get_url(search_item)

    for page in range(1, 6):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)

    for i in records:
        records_api.append({
            'title': list(i)[0],
            'price': list(i)[1],
            'rating': list(i)[2],
            'review_count': list(i)[3],
            'url': list(i)[4]
        })
    driver.close()
    return records_api
