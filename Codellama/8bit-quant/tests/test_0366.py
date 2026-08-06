import json

import pytest
from src_0366 import task_func


def test_task_func_valid_input():
    n = 5
    file_name = 'test_output.json'
    seed = 77
    task_func(n, file_name, seed)
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert len(data) == n
    assert all(word in WORDS for word in data.keys())
    assert all(data[word] == 1 for word in data.keys())

def test_task_func_invalid_input():
    n = 0
    file_name = 'test_output.json'
    seed = 77
    with pytest.raises(ValueError):
        task_func(n, file_name, seed)

def test_task_func_random_seed():
    n = 5
    file_name = 'test_output.json'
    seed = 77
    task_func(n, file_name, seed)
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert len(data) == n
    assert all(word in WORDS for word in data.keys())
    assert all(data[word] == 1 for word in data.keys())

    seed = 123
    task_func(n, file_name, seed)
    with open(file_name, 'r') as f:
        data = json.load(f)
    assert len(data) == n
    assert all(word in WORDS for word in data.keys())
    assert all(data[word] == 1 for word in data.keys())

    assert data != data_prev