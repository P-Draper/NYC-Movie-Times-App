import requests
from bs4 import BeautifulSoup

class MetrographScraper:
    def __init__(self, url):
        self.url = url
    #takes in url argument
    def get_film_data(self):
        page = requests.get(self.url)
        #get and parse the data
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find()
        #target the specific element we want
        titles = results.find_all('h3', class_='movie_title')
        #go to the parent so we can iterate through the children later
        title_elements = [h3_element.parent for h3_element in titles]
        #create an empty array to be appended to
        film_data = []
        #iterate through and target individual elements
        for film_element in title_elements:
            title_element = film_element.find('h3', class_='movie_title')
            synopsis_element = film_element.find('p', class_='synopsis')
            date_element = film_element.find('h5', class_='sr-only')  # Needs improvement to find all dates, not just default
            #append the elements
            film_data.append(
                {
                    "Title": title_element.text.strip(),
                    "Synopsis": synopsis_element.text.strip(),
                    "Date": date_element.text.strip()
                }
            )

        return film_data
    '''
    def soup_test(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find()
        titles = results.find_all('h3', class_='movie_title')
        title_elements = [h3_element.parent for h3_element in titles]
        print(title_elements)
    '''