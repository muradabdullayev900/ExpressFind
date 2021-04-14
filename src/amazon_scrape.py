from bs4 import BeautifulSoup
from selenium import webdriver


def get_url(search_term):
    template = f'https://www.amazon.com/s?k={search_term}&crid=2LVUHRLNH01PN&sprefix=ultrawide%2Caps%2C354&ref=nb_sb_ss_ts-doa-p_1_9'
    search_term = search_term.replace(' ', '+')
    return template


def extract_record(item):
    try:
        atag = item.h2.a
        title = atag.text.strip()
        url = 'https://amazon.com' + atag.get('href')
    except AttributeError:
        title = 'No title provided'

    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        price = 'no price'

    try:
        rating = item.i.text
    except AttributeError:
        rating = 'no rating'

    result = {
        'title': title,
        'price': price,
        'rating': rating,
        'url': url
    }

    return result


def main(search_item):
    driver = webdriver.Chrome('D:/Compressed/chromedriver.exe')

    records = []

    url = get_url(search_item)

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})

    for item in results:
        record = extract_record(item)
        if record:
            records.append(record)

    driver.quit()
    return records


if __name__ == '__main__':
    main()