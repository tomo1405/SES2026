import pytest
from src_0160 import task_func
import numpy as np

def test_task_func_with_empty_array():
    newArray = np.array([], dtype=np.float64)
    result = task_func(newArray)
    assert result == b''

def test_task_func_with_single_element():
    newArray = np.array([3.14], dtype=np.float64)
    result = task_func(newArray)
    expected = gzip.compress(struct.pack('d', 3.14))
    assert result == expected

def test_task_func_with_multiple_elements():
    newArray = np.array([1.0, 2.0, 3.0], dtype=np.float64)
    result = task_func(newArray)
    expected = gzip.compress(struct.pack('ddd', 1.0, 2.0, 3.0))
    assert result == expected

def test_task_func_with_negative_numbers():
    newArray = np.array([-1.0, -2.0, -3.0], dtype=np.float64)
    result = task_func(newArray)
    expected = gzip.compress(struct.pack('ddd', -1.0, -2.0, -3.0))
    assert result == expected

def test_task_func_with_large_numbers():
    newArray = np.array([1e10, 2e10, 3e10], dtype=np.float64)
    result = task_func(newArray)
    expected = gzip.compress(struct.pack('ddd', 1e10, 2e10, 3e10))
    assert result == expected