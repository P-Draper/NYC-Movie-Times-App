import requests
from bs4 import BeautifulSoup

class SyndicatedScraper:
    def __init__(self, url):
        self.url = url
    #get request the url, parse and target the correct element
    def get_film_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find()
        titles = results.find_all('h3', class_='title')
        #grab the parent of the element so we can move through every child
        title_elements = [h3_element.parent for h3_element in titles]
        #our empty array to append to
        film_data = []
        #iterate through and pull the individual elements we want
        for film_element in title_elements:
            title_element = film_element.find('h3', class_='title')
            date_element = film_element.find('h4', class_='date')
            time_element = film_element.find('ul', class_='session-times')
            #append our dictionary
            film_data.append(
                {
                    "Title": title_element.text.strip(),
                    "Date": date_element.text.strip(),
                    "Time": time_element.text.strip()
                }
            )

        return film_data
    '''
    def soup_test(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find()
        titles = results.find_all('h3', class_='title')
        title_elements = [h3_element.parent for h3_element in titles]
        print(title_elements)
    '''