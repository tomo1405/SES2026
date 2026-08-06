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
    # Test case 1: Valid input file and delimiter
    assert task_func('test_data.csv', ',') == [('the', 2), ('quick', 1), ('brown', 1), ('fox', 1), ('jumps', 1), ('over', 1), ('lazy', 1)]

    # Test case 2: Invalid input file
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv', ',')

    # Test case 3: Invalid delimiter
    with pytest.raises(csv.Error):
        task_func('test_data.csv', ';')