import json

import pytest
from src_0366 import task_func


def test_task_func_valid_n(tmp_path):
    n = 3
    file_name = tmp_path / "test_output.json"
    result = task_func(n, file_name)
    assert result == str(file_name)

    with open(file_name, 'r') as f:
        data = json.load(f)
    
    assert set(data.keys()) <= set(['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew'])
    assert sum(data.values()) == n

def test_task_func_invalid_n():
    with pytest.raises(ValueError):
        task_func(0, "test_output.json")

def test_task_func_n_greater_than_words_length():
    with pytest.raises(ValueError):
        task_func(len(WORDS) + 1, "test_output.json")

def test_task_func_seed_consistency(tmp_path):
    n = 5
    file_name1 = tmp_path / "test_output1.json"
    file_name2 = tmp_path / "test_output2.json"
    
    task_func(n, file_name1)
    task_func(n, file_name2)
    
    with open(file_name1, 'r') as f1:
        data1 = json.load(f1)
    
    with open(file_name2, 'r') as f2:
        data2 = json.load(f2)
    
    assert data1 == data2

def test_task_func_randomness(tmp_path):
    n = 5
    file_name1 = tmp_path / "test_output1.json"
    file_name2 = tmp_path / "test_output2.json"
    
    task_func(n, file_name1, seed=1)
    task_func(n, file_name2, seed=2)
    
    with open(file_name1, 'r') as f1:
        data1 = json.load(f1)
    
    with open(file_name2, 'r') as f2:
        data2 = json.load(f2)
    
    assert data1 != data2