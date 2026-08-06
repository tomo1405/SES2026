import pytest
from src_0097 import task_func

def test_task_func():
    csv_file = 'test_data.csv'
    csv_delimiter = ','
    expected_result = [('word1', 3), ('word2', 2), ('word3', 1)]

    with open(csv_file, 'w') as f:
        f.write('word1,word2,word3\n')
        f.write('word1,word2,word3\n')
        f.write('word1,word2,word3\n')

    result = task_func(csv_file, csv_delimiter)

    assert result == expected_result