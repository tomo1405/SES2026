import pytest
from src_1019 import task_func

def test_task_func():
    # Test with valid URL and from_encoding
    url = "http://example.com"
    from_encoding = "cp1251"
    soup = task_func(url, from_encoding)
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)

    # Test with invalid URL
    url = None
    soup = task_func(url, from_encoding)
    assert soup is None

    # Test with invalid from_encoding
    url = "http://example.com"
    from_encoding = None
    soup = task_func(url, from_encoding)
    assert soup is None

    # Test with use_lxml=True
    url = "http://example.com"
    from_encoding = "cp1251"
    soup = task_func(url, from_encoding, use_lxml=True)
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)
    assert soup.parser == "lxml"

    # Test with use_lxml=False
    url = "http://example.com"
    from_encoding = "cp1251"
    soup = task_func(url, from_encoding, use_lxml=False)
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)
    assert soup.parser == "html.parser"