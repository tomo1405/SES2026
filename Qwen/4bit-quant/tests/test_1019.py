import pytest
import requests
from bs4 import BeautifulSoup
from src_1019 import task_func


def test_task_func_default_url():
    soup = task_func()
    assert isinstance(soup, BeautifulSoup)

def test_task_func_custom_url():
    custom_url = "http://example.org"
    soup = task_func(custom_url)
    assert isinstance(soup, BeautifulSoup)

def test_task_func_invalid_url():
    invalid_url = "http://nonexistenturl123.com"
    soup = task_func(invalid_url)
    assert soup is None

def test_task_func_timeout():
    with pytest.raises(requests.exceptions.Timeout):
        task_func("http://example.com", timeout=0.001)

def test_task_func_lxml_parser():
    soup = task_func(use_lxml=True)
    assert isinstance(soup, BeautifulSoup)
    assert soup.parser == 'lxml'

def test_task_func_html_parser():
    soup = task_func(use_lxml=False)
    assert isinstance(soup, BeautifulSoup)
    assert soup.parser == 'html.parser'

def test_task_func_no_url():
    soup = task_func(url="")
    assert soup is None

def test_task_func_decoding_error():
    with pytest.raises(UnicodeDecodeError):
        task_func(from_encoding="invalid_encoding")