python
import pandas as pd
import pytest
from itertools import combinations
from src_0705 import task_func

# Constants
MIN_PERCENTAGE = 0.75

# Test case 1
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.8
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 2
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.5
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_2():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 3
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 1.0
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_3():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 4
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.25
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_4():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 5
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.0
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_5():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 6
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 1.5
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_6():
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

# Test case 7
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = -0.5
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_7():
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

# Test case 8
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = '0.5'
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c')]

def test_task_func_8():
    with pytest.raises(ValueError):
        task_func(data, cols, percentage)

# Test case 9
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.5
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]

def test_task_func_9():
    result = task_func(data, cols, percentage)
    assert result == expected_result

# Test case 10
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cols = ['a', 'b', 'c']
percentage = 0.5
expected_result = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('a', 'b', 'c')]

def test_task_func_10():
    result = task_func(data, cols, percentage)
    assert result == expected_result