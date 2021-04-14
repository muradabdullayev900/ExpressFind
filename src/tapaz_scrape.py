from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_term):
    template = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={search_term}&q%5Bregion_id%5D='
    search_term = search_term.replace(' ', '+')
    return template


def extract_record(item):
    try:
        atag = item.a
        title = item.find('div', {'class': 'products-name'}).text.strip()
        url = 'https://tap.az' + atag.get('href')[:-9]
    except AttributeError:
        title = 'No title provided'

    try:
        price_parent = item.find('div', {'class': 'products-price'})
        price = price_parent.find('span', {'class': 'price-val'}).text.strip() + ' ' + price_parent.find('span', {'class': 'price-cur'}).text.strip()
    except AttributeError:
        price = 'no price'

    result = {
        'title': title,
        'price': price,
        'url': url,
        'source': 'tap.az'
    }

    return result


def tapaz_scraper(search_item):
    driver = webdriver.Chrome('D:/Compressed/chromedriver.exe')

    records = []

    url = get_url(search_item)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'class': "products-i rounded"}) + soup.find_all('div', {'class': "products-i rounded bumped products-shop"}) + soup.find_all('div', {'class': "products-i rounded bumped"})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)

    driver.quit()
    return records


if __name__ == "__tapaz_scraper__":
    tapaz_scraper()
