import pytest
from src_0328 import task_func

def test_task_func():
    file_path = 'test_data.csv'
    regex_pattern = r'\(.+?\)|\w+|[\W_]+'
    expected_result = {'word1': 2, 'word2': 3, 'word3': 1}

    with open(file_path, 'w') as file:
        file.write('word1,word2,word3\n')
        file.write('word1,word2,word3\n')
        file.write('word1,word2,word3\n')

    result = task_func(file_path, regex_pattern)

    assert result == expected_result