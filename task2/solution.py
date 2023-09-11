import requests
import collections
import csv

from bs4 import BeautifulSoup
from bs4.element import Tag


class ParseAnimals:
    def __init__(self) -> None:
        self.animals_names = {}

    def parse(self) -> None:
        """
            Make a while loop until calegory letter != Я
            Saves each animal data on the page in dict: key - letter, value - list of all animals on the page
        """
        url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        letter = ''

        while letter != 'Я':
            data = self._get_page(url)
            self._parse_animal_on_page(data=data)
            url = self._check_end_page(data=data)

            letter = collections.deque(self.animals_names, maxlen=1)[0][0]
            print(letter)

        self._get_csv()


    def _get_page(self, url: str) -> Tag:
        """
            Make a request on the page and gets all page data
        """
        request = requests.get(url)
        soup = BeautifulSoup(request.text, 'lxml')

        return soup.find('div', id='mw-pages')
    
    def _parse_animal_on_page(self, data: Tag) -> None:
        """
            Saves all animals on the page in a dict with key = category (letter)
        """
        for el in data.find_all('div', class_='mw-category-group'):
            category = el.h3.text
            animal_names = [[i.text, f"https://ru.wikipedia.org{i.a['href']}"] for i in el.find_all('li')]

            if not self.animals_names.get(category):
                self.animals_names[category] = []

            self.animals_names[category] = self.animals_names[category] + animal_names

    def _check_end_page(self, data: Tag) -> str:
        """
            Return an url to the next page
        """
        hrf = data.find_all('a')[-1]
        return f"https://ru.wikipedia.org{hrf['href']}"
    
    def _get_csv(self) -> None:
        """
            Saves data (dict) into csv file
        """
        with open('animals_names_count.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows([[f'{k}, {len(v)}'] for k, v in self.animals_names.items()])
    

if __name__ == '__main__':
    parse = ParseAnimals()
    parse.parse()