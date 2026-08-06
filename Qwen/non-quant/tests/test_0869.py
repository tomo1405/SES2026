import pytest
from src_0869 import task_func
from itertools import cycle
from random import choice, seed

def test_task_func_default_colors():
    result = task_func(5)
    assert len(result) == 5
    assert all(color in ['Red', 'Green', 'Blue', 'Yellow', 'Purple'] for color in result)

def test_task_func_custom_colors():
    custom_colors = ['Black', 'White', 'Gray']
    result = task_func(6, custom_colors)
    assert len(result) == 6
    assert all(color in custom_colors for color in result)

def test_task_func_even_index_cycle():
    result = task_func(10)
    assert result[0] == 'Red'
    assert result[2] == 'Blue'
    assert result[4] == 'Yellow'
    assert result[6] == 'Purple'
    assert result[8] == 'Red'

def test_task_func_odd_index_random():
    result = task_func(10)
    assert result[1] in ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
    assert result[3] in ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
    assert result[5] in ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
    assert result[7] in ['Red', 'Green', 'Blue', 'Yellow', 'Purple']
    assert result[9] in ['Red', 'Green', 'Blue', 'Yellow', 'Purple']

def test_task_func_with_seed():
    seed_value = 42
    result1 = task_func(10, rng_seed=seed_value)
    result2 = task_func(10, rng_seed=seed_value)
    assert result1 == result2

def test_task_func_zero_colors():
    result = task_func(0)
    assert result == []

def test_task_func_one_color():
    result = task_func(1)
    assert len(result) == 1
    assert result[0] == 'Red'

def test_task_func_negative_colors():
    with pytest.raises(ValueError):
        task_func(-1)