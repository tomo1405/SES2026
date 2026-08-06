import mechanize
from bs4 import BeautifulSoup
from src_0285 import task_func


def test_task_func():
    url = "https://www.example.com"
    br = mechanize.Browser()
    response = br.open(url)
    soup = BeautifulSoup(response.read(), 'html.parser')

    links = [urljoin(url, a['href']) for a in soup.find_all('a', href=True)]

    assert task_func(url) == links