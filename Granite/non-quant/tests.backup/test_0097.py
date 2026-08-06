import pytest
from src_0097 import task_func

def test_task_func():
    csv_file = 'path/to/csv_file.csv'
    csv_delimiter = ','
    expected_output = [
        (['word1', 'word2', 'word3'], 10),
        (['word4', 'word5', 'word6'], 8),
        (['word7', 'word8', 'word9'], 6)
    ]
    actual_output = task_func(csv_file, csv_delimiter)
    assert actual_output == expected_output