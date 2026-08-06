import pytest
from src_0192 import task_func
from scipy import stats

def test_task_func_empty_animals():
    assert task_func([], 5) == {}

def test_task_func_single_animal():
    result = task_func(['dog'], 5)
    assert len(result) == 1
    assert 'dog' in result
    assert result['dog'] >= 0

def test_task_func_multiple_animals():
    result = task_func(['cat', 'dog', 'bird'], 5)
    assert len(result) == 3
    for animal in ['cat', 'dog', 'bird']:
        assert animal in result
        assert result[animal] >= 0

def test_task_func_mean_zero():
    result = task_func(['cat', 'dog'], 0)
    assert all(value == 0 for value in result.values())

def test_task_func_mean_high():
    result = task_func(['cat', 'dog'], 100)
    assert any(value > 0 for value in result.values())

def test_task_func_mean_medium():
    result = task_func(['cat', 'dog'], 10)
    assert sum(result.values()) == stats.poisson(mu=10).rvs()

def test_task_func_consistency():
    animals = ['cat', 'dog']
    mean = 5
    results = [task_func(animals, mean) for _ in range(10)]
    for result in results:
        assert len(result) == 2
        for animal in animals:
            assert animal in result
            assert result[animal] >= 0