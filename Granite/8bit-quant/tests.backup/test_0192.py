import random
from scipy import stats
from src_0192 import task_func

def test_task_func_with_no_animals():
    animals = []
    mean = 10
    expected_sales = {}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

def test_task_func_with_one_animal():
    animals = ['dog']
    mean = 10
    expected_sales = {'dog': 0}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

def test_task_func_with_multiple_animals():
    animals = ['dog', 'cat', 'bird']
    mean = 10
    expected_sales = {'dog': 0, 'cat': 0, 'bird': 0}
    actual_sales = task_func(animals, mean)
    assert actual_sales == expected_sales

def test_task_func_with_random_animals_and_mean():
    animals = ['dog', 'cat', 'bird', 'fish']
    mean = 5
    expected_sales = {}
    for _ in range(100):
        actual_sales = task_func(animals, mean)
        for animal in animals:
            expected_sales[animal] = expected_sales.get(animal, 0) + 1
        assert actual_sales == expected_sales
        expected_sales = {}