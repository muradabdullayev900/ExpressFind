# How the Business Layer works

#### The main idea of this project is to scrape data from two commercial sites (amazon.com and tap.az) and use api for the third site (aliexpress.com) according to the item that user wants to search for. 
#### Selenium webdriver and beautiful soup is used for webscraping and RapidApi for aliexpress. 

#### Scraper class has 3 child classes that two(amazon and tapaz) scrapes the data and one(aliexpress) uses api. Displayer class filters data according to the sorting type, currency and minimum, maximum price.

#### Driver class provides driver for the scraper classes

#### More detailed information can be found in uml class diagram below:

![Flask _Project](https://user-images.githubusercontent.com/71690814/118007675-67383780-b35d-11eb-9f54-e342e2ecac01.png)