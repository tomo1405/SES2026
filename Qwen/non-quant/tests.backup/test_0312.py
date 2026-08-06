import pytest
from src_0312 import task_func
import numpy as np
from scipy import stats

def test_task_func_with_non_empty_lists():
    list_of_lists = [[1, 2, 3], [4, 5, 6]]
    result = task_func(list_of_lists)
    assert result['mean'] == np.mean([1, 2, 3, 4, 5, 6])
    assert result['median'] == np.median([1, 2, 3, 4, 5, 6])
    assert result['mode'] == stats.mode([1, 2, 3, 4, 5, 6])[0]

def test_task_func_with_empty_lists():
    list_of_lists = [[], []]
    result = task_func(list_of_lists)
    expected_data = [random.randint(0, 100) for _ in range(10)]
    assert result['mean'] == np.mean(expected_data)
    assert result['median'] == np.median(expected_data)
    assert result['mode'] == stats.mode(expected_data)[0]

def test_task_func_with_mixed_lists():
    list_of_lists = [[1, 2, 3], [], [4, 5, 6]]
    result = task_func(list_of_lists)
    expected_data = [1, 2, 3] + [random.randint(0, 100) for _ in range(5)] + [4, 5, 6]
    assert result['mean'] == np.mean(expected_data)
    assert result['median'] == np.median(expected_data)
    assert result['mode'] == stats.mode(expected_data)[0]

def test_task_func_with_custom_size():
    list_of_lists = [[1, 2, 3], []]
    result = task_func(list_of_lists, size=3)
    expected_data = [1, 2, 3] + [random.randint(0, 100) for _ in range(3)]
    assert result['mean'] == np.mean(expected_data)
    assert result['median'] == np.median(expected_data)
    assert result['mode'] == stats.mode(expected_data)[0]

def test_task_func_with_custom_seed():
    list_of_lists = [[1, 2, 3], []]
    result = task_func(list_of_lists, seed=42)
    expected_data = [1, 2, 3] + [random.randint(0, 100) for _ in range(5)]
    assert result['mean'] == np.mean(expected_data)
    assert result['median'] == np.median(expected_data)
    assert result['mode'] == stats.mode(expected_data)[0]