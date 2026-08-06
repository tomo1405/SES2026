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
    url = 'https://www.example.com'
    expected_occurrences = 0

    occurrences = task_func(url)

    assert occurrences == expected_occurrences