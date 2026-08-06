import pytest
from src_0192 import task_func

def test_task_func():
    animals = ['dog', 'cat', 'bird']
    mean = 2
    expected_sales = {'dog': 1, 'cat': 1, 'bird': 0}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

def test_task_func_with_no_animals():
    animals = []
    mean = 2
    expected_sales = {}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

def test_task_func_with_one_animal():
    animals = ['dog']
    mean = 2
    expected_sales = {'dog': 2}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales