import mechanize
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def task_func(url):
    br = mechanize.Browser()
    response = br.open(url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

    return links