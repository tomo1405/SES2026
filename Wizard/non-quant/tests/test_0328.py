python
import csv
import re
from collections import Counter
import pytest

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        text = ' '.join(row[0] for row in reader)
        matches = re.findall(regex_pattern, text)

    counts = Counter(matches)
    return dict(counts)

def test_task_func():
    # Test case 1: default regex pattern
    assert task_func('test_data.csv') == {'(': 1, 'w': 2, 'o': 2, 'r': 1, 'l': 1, 'd': 1, '_': 1, 't': 1, 'e': 1, 's': 1, 't': 1, 'c': 1, 'a': 1, 's': 1, 'v': 1, 'f': 1, 'i': 1, 'l': 1, 'e': 1, '.': 1}

    # Test case 2: custom regex pattern
    assert task_func('test_data.csv', regex_pattern=r'\w+') == {'word': 1, 'test': 1, 'csv': 1, 'file': 1}