import pytest
from src_0192 import task_func
from scipy import stats
import random

def test_task_func_no_animals():
    assert task_func([], 5) == {}

def test_task_func_single_animal():
    result = task_func(['dog'], 5)
    assert len(result) == 1
    assert 'dog' in result
    assert result['dog'] >= 0

def test_task_func_multiple_animals():
    result = task_func(['dog', 'cat'], 5)
    assert len(result) == 2
    assert 'dog' in result
    assert 'cat' in result
    assert result['dog'] >= 0
    assert result['cat'] >= 0

def test_task_func_mean_zero():
    result = task_func(['dog', 'cat'], 0)
    assert len(result) == 2
    assert 'dog' in result
    assert 'cat' in result
    assert result['dog'] == 0
    assert result['cat'] == 0

def test_task_func_mean_large():
    result = task_func(['dog', 'cat'], 100)
    assert len(result) == 2
    assert 'dog' in result
    assert 'cat' in result
    assert result['dog'] >= 0
    assert result['cat'] >= 0

def test_task_func_randomness():
    random.seed(42)
    result1 = task_func(['dog', 'cat'], 5)
    random.seed(42)
    result2 = task_func(['dog', 'cat'], 5)
    assert result1 == result2

def test_task_func_poisson_distribution():
    random.seed(42)
    num_customers = stats.poisson(mu=5).rvs()
    assert num_customers >= 0