import pytest
from src_0192 import task_func

def test_task_func():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_with_customers():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_with_invalid_input():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_with_empty_input():
    animals = []
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {}