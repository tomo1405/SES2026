import json
import os

import pytest
from src_0366 import task_func


@pytest.fixture
def temp_file_name():
    return "temp_test_file.json"

def test_task_func_valid_n(temp_file_name):
    n = 3
    result = task_func(n, temp_file_name)
    assert result == temp_file_name
    with open(result, 'r') as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert len(data) == n

def test_task_func_min_n(temp_file_name):
    n = 1
    result = task_func(n, temp_file_name)
    assert result == temp_file_name
    with open(result, 'r') as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert len(data) == n

def test_task_func_max_n(temp_file_name):
    n = len(WORDS)
    result = task_func(n, temp_file_name)
    assert result == temp_file_name
    with open(result, 'r') as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert len(data) == n

def test_task_func_invalid_n(temp_file_name):
    with pytest.raises(ValueError):
        task_func(0, temp_file_name)
    with pytest.raises(ValueError):
        task_func(len(WORDS) + 1, temp_file_name)

def test_task_func_randomness(temp_file_name):
    n = 5
    result1 = task_func(n, temp_file_name, seed=123)
    with open(result1, 'r') as f:
        data1 = json.load(f)
    
    result2 = task_func(n, temp_file_name, seed=456)
    with open(result2, 'r') as f:
        data2 = json.load(f)
    
    assert data1 != data2

def test_task_func_reproducibility(temp_file_name):
    n = 5
    result1 = task_func(n, temp_file_name, seed=77)
    with open(result1, 'r') as f:
        data1 = json.load(f)
    
    result2 = task_func(n, temp_file_name, seed=77)
    with open(result2, 'r') as f:
        data2 = json.load(f)
    
    assert data1 == data2

def test_task_func_cleanup(temp_file_name):
    n = 3
    task_func(n, temp_file_name)
    assert os.path.exists(temp_file_name)
    os.remove(temp_file_name)
    assert not os.path.exists(temp_file_name)