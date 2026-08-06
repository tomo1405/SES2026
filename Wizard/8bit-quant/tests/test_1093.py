python
import ast
import requests
from bs4 import BeautifulSoup
import pytest

def task_func(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for script in soup.find_all('script'):
        try:
            results.append(ast.literal_eval(script.string))
        except (ValueError, SyntaxError):
            continue

    return results

def test_task_func():
    # Test case 1
    url = 'https://www.example.com'
    expected_result = []
    assert task_func(url) == expected_result

    # Test case 2
    url = 'https://www.python.org'
    expected_result = [{'type': 'text/javascript', 'src': 'https://www.python.org/static/js/site.js'}]
    assert task_func(url) == expected_result

    # Test case 3
    url = 'https://www.google.com'
    expected_result = []
    assert task_func(url) == expected_result