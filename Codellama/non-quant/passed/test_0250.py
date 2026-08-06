import pytest
from src_0250 import task_func

def test_task_func_n_data_points():
    train_data, test_data = task_func(n_data_points=10000)
    assert len(train_data) == 8000
    assert len(test_data) == 2000

def test_task_func_min_value():
    train_data, test_data = task_func(min_value=0.0)
    assert all(train_data['Value'] >= 0.0)
    assert all(test_data['Value'] >= 0.0)

def test_task_func_max_value():
    train_data, test_data = task_func(max_value=10.0)
    assert all(train_data['Value'] <= 10.0)
    assert all(test_data['Value'] <= 10.0)

def test_task_func_test_size():
    train_data, test_data = task_func(test_size=0.2)
    assert len(train_data) == 8000
    assert len(test_data) == 2000

def test_task_func_random_data():
    train_data, test_data = task_func()
    assert len(train_data) == 8000
    assert len(test_data) == 2000
    assert all(train_data['Value'] >= 0.0)
    assert all(train_data['Value'] <= 10.0)
    assert all(test_data['Value'] >= 0.0)
    assert all(test_data['Value'] <= 10.0)