import requests
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.url = 'https://www.strawberryhouse.uz/ru'
        self.host = 'https://www.strawberryhouse.uz'

    def get_html(self, url=None):
        if url:
            return requests.get(url).text
        else:
            return requests.get(self.url).text

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')



