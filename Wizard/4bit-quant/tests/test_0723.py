python
import urllib.request
import os
import re
import pytest

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    urllib.request.urlretrieve(url, TARGET_FILE)

    with open(TARGET_FILE, 'r') as f:
        data = f.read()
    occurrences = len(re.findall(SEARCH_PATTERN, data))

    os.remove(TARGET_FILE)

    return occurrences

def test_task_func():
    # Test case 1
    url = 'https://www.google.com'
    expected_occurrences = 0
    actual_occurrences = task_func(url)
    assert actual_occurrences == expected_occurrences

    # Test case 2
    url = 'https://www.example.com'
    expected_occurrences = 1
    actual_occurrences = task_func(url)
    assert actual_occurrences == expected_occurrences

    # Test case 3
    url = 'https://www.python.org'
    expected_occurrences = 2
    actual_occurrences = task_func(url)
    assert actual_occurrences == expected_occurrences