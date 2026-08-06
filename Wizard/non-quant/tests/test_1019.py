python
import pytest
from src_1019 import task_func

def test_task_func():
    # Test case 1: Valid URL, default encoding, default parser
    soup = task_func(url="http://example.com")
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)

    # Test case 2: Invalid URL, default encoding, default parser
    soup = task_func(url="http://invalid.url")
    assert soup is None

    # Test case 3: Valid URL, custom encoding, default parser
    soup = task_func(url="http://example.com", from_encoding="utf-8")
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)

    # Test case 4: Valid URL, custom encoding, custom parser
    soup = task_func(url="http://example.com", from_encoding="utf-8", use_lxml=True)
    assert soup is not None
    assert isinstance(soup, BeautifulSoup)

    # Test case 5: Valid URL, invalid encoding, default parser
    soup = task_func(url="http://example.com", from_encoding="invalid")
    assert soup is None

    # Test case 6: Valid URL, invalid encoding, custom parser
    soup = task_func(url="http://example.com", from_encoding="invalid", use_lxml=True)
    assert soup is None