import mechanize
from bs4 import BeautifulSoup


def test_task_func():
    url = 'https://www.example.com'
    br = mechanize.Browser()
    response = br.open(url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

    assert links == [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]