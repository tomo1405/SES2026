import pytest
from src_0102 import task_func

def test_task_func():
    assert task_func() is not None

def test_task_func_with_data_url():
    assert task_func(data_url="http://lib.stat.cmu.edu/datasets/boston") is not None

def test_task_func_with_seed():
    assert task_func(seed=42) is not None

def test_task_func_with_data_url_and_seed():
    assert task_func(data_url="http://lib.stat.cmu.edu/datasets/boston", seed=42) is not None

def test_task_func_with_invalid_data_url():
    with pytest.raises(ValueError):
        task_func(data_url="invalid_url")

def test_task_func_with_invalid_seed():
    with pytest.raises(ValueError):
        task_func(seed="invalid_seed")