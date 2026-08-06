import pytest
from src_0900 import task_func

def test_task_func_length_negative():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_length_zero():
    walk = task_func(length=0)
    assert walk == [0]

def test_task_func_length_positive():
    walk = task_func(length=10000)
    assert len(walk) == 10001
    assert walk[0] == 0
    assert walk[-1] == 0

def test_task_func_seed():
    walk1 = task_func(length=10000, seed=0)
    walk2 = task_func(length=10000, seed=0)
    assert walk1 == walk2

    walk3 = task_func(length=10000, seed=1)
    assert walk1 != walk3