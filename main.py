from urllib.request import urlopen
from bs4 import BeautifulSoup


class URLdownloader():
    url = 'https://www.mobilmax.cz/mobily?=1,1&pg='
    baseurl = "https://www.mobilmax.cz"
    filename = 'urls.txt'
    filename2 = 'data.tsv'

    def get_webpage(self, url, i):
        full_url = url + str(i)
        page = urlopen(full_url)
        return page

    def file_open(self, filename):
        return open(filename, 'w')

    def file_close(file):
        file.close()

    def parse(self, file, limit):
        prdctnum = 0
        for i in range(1, 6):
            page = self.get_webpage(self.url, i)
            html = page.read().decode("utf-8")
            soup = BeautifulSoup(html, "html.parser")
            links = soup.findAll('a', class_='imageproduct')
            for link in links:
                prdctnum += 1
                file.write(self.baseurl + '/' + link.get('href'))
                if prdctnum == limit:
                    return
                file.write('\n')

    def parse_example(self):
        file = self.file_open('urls.txt')
        self.parse(file, 150)
        file.close()

    def test_parse(self):
        file = self.file_open('url_test.txt')
        self.parse(file, 10)
        file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = URLdownloader()
    d.parse_example()
    d.test_parse()
