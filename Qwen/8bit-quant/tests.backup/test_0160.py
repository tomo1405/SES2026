import pytest
from src_0160 import task_func
import numpy as np

def test_task_func_with_empty_array():
    newArray = np.array([])
    result = task_func(newArray)
    assert result == b''

def test_task_func_with_single_element():
    newArray = np.array([3.14])
    expected = gzip.compress(struct.pack('d', 3.14))
    result = task_func(newArray)
    assert result == expected

def test_task_func_with_multiple_elements():
    newArray = np.array([1.0, 2.0, 3.0])
    expected = gzip.compress(struct.pack('ddd', 1.0, 2.0, 3.0))
    result = task_func(newArray)
    assert result == expected

def test_task_func_with_large_array():
    newArray = np.random.rand(1000)
    result = task_func(newArray)
    assert isinstance(result, bytes)
    assert len(result) > 0

def test_task_func_with_negative_values():
    newArray = np.array([-1.5, -2.5, -3.5])
    expected = gzip.compress(struct.pack('ddd', -1.5, -2.5, -3.5))
    result = task_func(newArray)
    assert result == expected

def test_task_func_with_zero_values():
    newArray = np.array([0.0, 0.0, 0.0])
    expected = gzip.compress(struct.pack('ddd', 0.0, 0.0, 0.0))
    result = task_func(newArray)
    assert result == expected