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
    # Test case 1: Valid input file and regex pattern
    file_path = 'input.csv'
    regex_pattern = r'\w+'
    expected_output = {'hello': 1, 'world': 1}
    assert task_func(file_path, regex_pattern) == expected_output

    # Test case 2: Invalid input file
    file_path = 'invalid_file.txt'
    regex_pattern = r'\w+'
    with pytest.raises(FileNotFoundError):
        task_func(file_path, regex_pattern)

    # Test case 3: Invalid regex pattern
    file_path = 'input.csv'
    regex_pattern = r'[\d]+'
    with pytest.raises(re.error):
        task_func(file_path, regex_pattern)