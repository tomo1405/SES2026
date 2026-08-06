python
import heapq
import pytest
from sklearn.linear_model import LinearRegression
from src_0793 import task_func

def test_task_func():
    # Test case 1: Valid input
    df = {'feature': [1, 2, 3, 4, 5], 'target': [5, 4, 3, 2, 1]}
    feature = 'feature'
    target = 'target'
    n = 3
    expected_output = ([0, 1, 2], LinearRegression())
    assert task_func(df, feature, target, n) == expected_output

    # Test case 2: Invalid input - feature column not found
    df = {'target': [5, 4, 3, 2, 1]}
    feature = 'feature'
    target = 'target'
    n = 3
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)

    # Test case 3: Invalid input - target column not found
    df = {'feature': [1, 2, 3, 4, 5]}
    feature = 'feature'
    target = 'target'
    n = 3
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)

    # Test case 4: Invalid input - n is not a positive integer
    df = {'feature': [1, 2, 3, 4, 5], 'target': [5, 4, 3, 2, 1]}
    feature = 'feature'
    target = 'target'
    n = -3
    with pytest.raises(ValueError):
        task_func(df, feature, target, n)