import pytest
from src_0192 import task_func

def test_task_func_empty_animals():
    animals = []
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {}

def test_task_func_non_empty_animals():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_non_empty_animals_with_sales():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_non_empty_animals_with_sales_and_mean():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}

def test_task_func_non_empty_animals_with_sales_and_mean_and_num_customers():
    animals = ['cat', 'dog', 'fish']
    mean = 10
    sales = task_func(animals, mean)
    assert sales == {'cat': 0, 'dog': 0, 'fish': 0}