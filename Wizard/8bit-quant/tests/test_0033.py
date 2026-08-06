python
import requests
from bs4 import BeautifulSoup
import pytest

def task_func(url, tag):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_content = soup.find(tag)
    
    return tag_content.string if tag_content else None

def test_task_func():
    # Test case 1: Valid URL and tag
    url = 'https://www.example.com'
    tag = 'h1'
    expected_result = 'Example Domain'
    assert task_func(url, tag) == expected_result
    
    # Test case 2: Invalid URL
    url = 'https://www.invalidurl.com'
    tag = 'h1'
    expected_result = None
    assert task_func(url, tag) == expected_result
    
    # Test case 3: Invalid tag
    url = 'https://www.example.com'
    tag = 'invalidtag'
    expected_result = None
    assert task_func(url, tag) == expected_result