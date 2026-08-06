import pytest
from src_0930 import task_func
import numpy as np
from scipy import stats

def test_task_func_empty_string():
    result = task_func("")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    assert result[0].size == 0
    assert isinstance(result[1], float)
    assert np.isnan(result[1])

def test_task_func_single_character():
    result = task_func("a")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    assert result[0].size == 0
    assert isinstance(result[1], float)
    assert np.isnan(result[1])

def test_task_func_two_characters():
    result = task_func("ab")
    expected_difference = np.array([1])
    expected_entropy = stats.entropy(expected_difference)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    np.testing.assert_array_equal(result[0], expected_difference)
    assert isinstance(result[1], float)
    assert np.isclose(result[1], expected_entropy)

def test_task_func_multiple_characters():
    result = task_func("abc")
    expected_difference = np.array([1, 1])
    expected_entropy = stats.entropy(expected_difference)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    np.testing.assert_array_equal(result[0], expected_difference)
    assert isinstance(result[1], float)
    assert np.isclose(result[1], expected_entropy)

def test_task_func_non_ascii_characters():
    result = task_func("你好")
    expected_difference = np.array([20652])
    expected_entropy = stats.entropy(expected_difference)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    np.testing.assert_array_equal(result[0], expected_difference)
    assert isinstance(result[1], float)
    assert np.isclose(result[1], expected_entropy)