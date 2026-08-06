import os
import csv
from collections import Counter
from src_0722 import task_func
import pytest

def test_task_func():
    file_path = "path/to/your/file.csv"
    expected_output = ("most_common_word", 10)

    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',', skipinitialspace=True)
        for row in csv_reader:
            for word in row:
                word_counter[word.strip()] += 1

    if not word_counter:
        return None

    most_common_word, frequency = word_counter.most_common(1)[0]
    assert task_func(file_path) == expected_output