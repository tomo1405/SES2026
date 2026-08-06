import pytest
from src_0160 import task_func
import numpy as np

def test_task_func_with_empty_array():
    newArray = np.array([])
    result = task_func(newArray)
    assert result == b''

def test_task_func_with_single_element():
    newArray = np.array([3.14])
    expected_result = gzip.compress(struct.pack('d', 3.14))
    result = task_func(newArray)
    assert result == expected_result

def test_task_func_with_multiple_elements():
    newArray = np.array([1.1, 2.2, 3.3])
    expected_result = gzip.compress(struct.pack('ddd', 1.1, 2.2, 3.3))
    result = task_func(newArray)
    assert result == expected_result

def test_task_func_with_large_numbers():
    newArray = np.array([1e10, 2e10, 3e10])
    expected_result = gzip.compress(struct.pack('ddd', 1e10, 2e10, 3e10))
    result = task_func(newArray)
    assert result == expected_result

def test_task_func_with_negative_numbers():
    newArray = np.array([-1.1, -2.2, -3.3])
    expected_result = gzip.compress(struct.pack('ddd', -1.1, -2.2, -3.3))
    result = task_func(newArray)
    assert result == expected_result

def test_task_func_with_zero():
    newArray = np.array([0.0, 0.0, 0.0])
    expected_result = gzip.compress(struct.pack('ddd', 0.0, 0.0, 0.0))
    result = task_func(newArray)
    assert result == expected_result