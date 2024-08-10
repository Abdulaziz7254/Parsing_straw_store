from time import time
from DataBase import Database
from BaseParser import Parser
from mixin import ProductDetailParser
class StrawberryParser(Database,Parser,ProductDetailParser):
    def __init__(self):
        Database.__init__(self),
        Parser.__init__(self),
        self.data = {}
    def get_data(self):
        self.db = Database
        soup = self.get_soup(self.get_html())
        nav = soup.find('ul',  class_='nav')
        categories = nav('li', class_='nav-item')
        for category in categories:
            self.db.create_categories_table(self)
            category_title = category.get_text(strip=True)
            category_href = self.host + category.find('a').get('href')
            self.db.save_category(self, category_title, category_href)
            self.products(category_href, category_title)
    def products(self, category_href, category_title):
        soup_product = self.get_soup(self.get_html(category_href))
        products = soup_product.find_all('div', class_='es-product-item')
        category_id = self.get_category_id(category_title)[0]
        for product in products:
            product_title = product.find('div',class_='es-product-title').get_text(strip=True)
            product_url =self.host +  product.find('a').get('href')
            product_price = int (''.join([i for i in product.find('div',class_='curr').get_text(strip=True) if i.isdigit()]))
            self.db.create_products_table(self)
            self.db.save_product(self, product_title, product_price, product_url, category_id)

def start_parsing():
    print('Парсер начал работу')
    start = time()
    parser = StrawberryParser()
    parser.get_data()
    finish = time()
    print(f'Парсер отработал за {finish - start} секунд')

start_parsing()



