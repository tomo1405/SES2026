import pytest
from src_0217 import task_func

def test_task_func():
    json_dir_path = 'path/to/json/dir'
    word_count = 10
    expected_result = [('word1', 10), ('word2', 8), ('word3', 6), ('word4', 4), ('word5', 2)]
    
    result = task_func(json_dir_path, word_count)
    
    assert result == expected_result