from bs4 import BeautifulSoup
from urllib.request import urlopen


class Paramsparser():

    def scrape_product(self, product_url, file, last):
        page = urlopen(product_url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        file.write(product_url + '\t')
        file.write(soup.find('h1', class_='product_title').string + '\t')
        file.write(soup.find('font', class_='c_price').get('data-defaultprice') + '\t')
        file.write(soup.find('font', class_='c_price_nodph').get('data-defaultprice-nodph') + '\t')
        file.write(soup.find('div', class_='productStock').dt.string + '\t')
        table = soup.find_all('table', class_='table table-hover paramTable')
        table = table[len(table)-1]
        rows = table.find_all('tr')
        for row in rows:
            file.write(row.td.string)
            if row != rows[len(rows)-1]:
                file.write('\t')

        if not last:
            file.write('\n')

    def print_product_info(self, product_url):
        page = urlopen(product_url+ '\t')
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        title = soup.find('h1', class_='product_title').string + '\t'
        priced = soup.find('font', class_='c_price').get('data-defaultprice') + '\t'
        nodph = soup.find('font', class_='c_price_nodph').get('data-defaultprice-nodph') + '\t'
        instock = soup.find('div', class_='productStock').dt.string + '\t'
        table = soup.find_all('table', class_='table table-hover paramTable')
        output = product_url + '\t' + title + priced + nodph + instock
        table = table[2]
        rows = table.find_all('tr')
        for row in rows:
            output += row.td.string
            if row != rows[len(rows)-1]:
                output += '\t'
        print(output)
    def create_example(self):
        filer = open('urls.txt', 'r')
        filew = open('data.tsv', 'w', encoding='utf-8')
        data = filer.read()
        lines = data.split('\n')
        for line in lines:
            self.scrape_product(line, filew,line == lines[len(lines)-1])
        filer.close()
        filew.close()

    def test(self):
        file = open('url_test.txt', 'r')
        data = file.read()
        lines = data.split('\n')
        for line in lines:
            self.print_product_info(line)

        file.close()


if __name__ == '__main__':
    parser = Paramsparser()
    #parser.create_example()
    parser.test()
