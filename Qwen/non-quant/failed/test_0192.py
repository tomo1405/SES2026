import pytest
from src_0192 import task_func
from scipy import stats
import random

def test_task_func_no_animals():
    assert task_func([], 5) == {}

def test_task_func_single_animal():
    result = task_func(['dog'], 5)
    assert 'dog' in result
    assert result['dog'] >= 0

def test_task_func_multiple_animals():
    animals = ['dog', 'cat', 'bird']
    result = task_func(animals, 5)
    for animal in animals:
        assert animal in result
        assert result[animal] >= 0

def test_task_func_mean_zero():
    animals = ['dog', 'cat']
    result = task_func(animals, 0)
    for animal in animals:
        assert result[animal] == 0

def test_task_func_mean_positive():
    animals = ['dog', 'cat']
    result = task_func(animals, 5)
    total_sales = sum(result.values())
    assert total_sales > 0

def test_task_func_randomness():
    animals = ['dog', 'cat']
    random.seed(42)
    result1 = task_func(animals, 5)
    random.seed(42)
    result2 = task_func(animals, 5)
    assert result1 == result2

def test_task_func_large_mean():
    animals = ['dog', 'cat']
    result = task_func(animals, 100)
    total_sales = sum(result.values())
    assert total_sales > 0

def test_task_func_negative_mean():
    with pytest.raises(ValueError):
        task_func(['dog'], -5)

def test_task_func_non_iterable_animals():
    with pytest.raises(TypeError):
        task_func('dog', 5)