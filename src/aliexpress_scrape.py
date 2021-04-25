from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_url(search_term):
    search_term = search_term.replace(' ', '+')
    template = f'https://aliexpress.ru/wholesale?catId=0&initiative_id=SB_20210414233356&SearchText={search_term}'
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
    chromeOptions.headless = False
    driver = webdriver.Chrome('D:/Compressed/chromedriver.exe', options=chromeOptions)

    records = []

    url = get_url(search_item)

    driver.get(url)
    # MAX_WAIT_TIME = 60
    # wait = WebDriverWait(driver, MAX_WAIT_TIME)
    # element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-info")))
    # height = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'class': 'product-card'})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)

    driver.quit()
    return records


if __name__ == "__aliexpress_scraper__":
    aliexpress_scraper()