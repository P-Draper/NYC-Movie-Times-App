import requests
from bs4 import BeautifulSoup
from mgscraper import MetrographScraper
from synscraper import SyndicatedScraper



page = requests.get('https://ticketing.useast.veezi.com/sessions/?siteToken=dxdq5wzbef6bz2sjqt83ytzn1c')
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find()
titles = results.find_all('h3', class_='title')#alter code from mgscraper
title_elements = [h3_element.parent for h3_element in titles]
#print(title_elements)
film_data = []

MetrographScraper.soup_test()

SyndicatedScraper.soup_test()

