import pytest
from src_0723 import task_func

def test_task_func():
    url = 'https://www.example.com/error_log.txt'
    occurrences = task_func(url)
    assert occurrences == 10

def test_task_func_with_invalid_url():
    url = 'https://www.example.com/invalid_log.txt'
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_with_invalid_search_pattern():
    url = 'https://www.example.com/error_log.txt'
    with pytest.raises(ValueError):
        task_func(url, search_pattern='invalid_pattern')