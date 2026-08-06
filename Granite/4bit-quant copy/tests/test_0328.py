import csv
import re
from collections import Counter
from src_0328 import task_func

def test_task_func():
    file_path = 'path/to/test/file.csv'
    regex_pattern = r'\(.+?\)|\w+|[\W_]+'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        text = ' '.join(row[0] for row in reader)
        matches = re.findall(regex_pattern, text)

    counts = Counter(matches)
    expected_result = {'apple': 1, 'banana': 2, 'cherry': 3}
    assert task_func(file_path, regex_pattern) == expected_result

def test_task_func_default_regex_pattern():
    file_path = 'path/to/test/file.csv'
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        text = ' '.join(row[0] for row in reader)
        matches = re.findall(r'\(.+?\)|\w+|[\W_]+', text)

    counts = Counter(matches)
    expected_result = {'apple': 1, 'banana': 2, 'cherry': 3}
    assert task_func(file_path) == expected_result