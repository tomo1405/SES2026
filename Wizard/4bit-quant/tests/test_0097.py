python
import csv
from collections import Counter
import operator
import pytest

def task_func(csv_file, csv_delimiter):
    words = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        for row in reader:
            words.extend(row)

    word_counter = Counter(words)
    most_common_words = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)

    return most_common_words

def test_task_func():
    # Test case 1
    csv_file = "test_file.csv"
    csv_delimiter = ","
    expected_result = [('the', 3), ('is', 2), ('a', 1)]
    assert task_func(csv_file, csv_delimiter) == expected_result

    # Test case 2
    csv_file = "test_file2.csv"
    csv_delimiter = ";"
    expected_result = [('the', 2), ('is', 1), ('a', 1)]
    assert task_func(csv_file, csv_delimiter) == expected_result