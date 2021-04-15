from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def get_url(search_term):
    template = f'https://aliexpress.ru/wholesale?catId=0&initiative_id=SB_20210414233356&SearchText={search_term}'
    search_term = search_term.replace(' ', '+')
    return template


def extract_record(item):
    try:
        atag = item.a
        title = item.find('div', {'class': 'item-title-wrap'}).text.strip()
        url = 'https:' + atag.get('href')
    except AttributeError:
        title = 'No title provided'

    try:
        price = item.find('span', {'class': 'price-current'}).text.strip()
    except AttributeError:
        price = 'no price'

    try:
        rating = item.find('span', {'class': 'rating-value'}).text + ' out of 5'
    except AttributeError:
        rating = 'no rating'

    result = {
        'title': title,
        'price': price,
        'rating': rating,
        'url': url,
        'source': 'aliexpress.ru'
    }

    return result


def aliexpress_scraper(search_item):
    chromeOptions = Options()
    chromeOptions.headless = True
    driver = webdriver.Chrome('D:/Compressed/chromedriver.exe', options=chromeOptions)

    records = []

    url = get_url(search_item)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'class': 'gallery product-card middle-place'})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)

    driver.quit()
    return records


if __name__ == "__aliexpress_scraper__":
    aliexpress_scraper()
