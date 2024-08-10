class ProductDetailParser:

    def get_product_characts(self, soup):
        characts = ''
        try:
            block = soup.find('div', class_='characteristics')
            lines = block.find_all('tr')
            for line in lines:
                left = line.find('td', class_='text-left').get_text(strip=True)
                right = line.find('td', class_='text-right').get_text(strip=True)
                characts += f'{left}: {right}\n'
        except:
            characts = 'Нет характеристик'
        return characts