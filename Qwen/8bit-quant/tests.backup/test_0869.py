import pytest
from src_0869 import task_func

def test_task_func_default_colors():
    assert task_func(5) == ['Red', 'Green', 'Blue', 'Yellow', 'Purple']

def test_task_func_custom_colors():
    custom_colors = ['Black', 'White', 'Gray']
    assert task_func(6, custom_colors) == ['Black', 'Gray', 'Black', 'White', 'Black', 'Gray']

def test_task_func_even_n_colors():
    assert task_func(4) == ['Red', 'Green', 'Red', 'Green']

def test_task_func_odd_n_colors():
    assert task_func(3) == ['Red', 'Green', 'Red']

def test_task_func_with_seed():
    seed_value = 42
    assert task_func(5, rng_seed=seed_value) == ['Red', 'Purple', 'Red', 'Green', 'Red']

def test_task_func_with_different_seed():
    seed_value = 123
    assert task_func(5, rng_seed=seed_value) == ['Red', 'Purple', 'Red', 'Blue', 'Red']

def test_task_func_single_color():
    assert task_func(1) == ['Red']

def test_task_func_no_colors():
    assert task_func(0) == []