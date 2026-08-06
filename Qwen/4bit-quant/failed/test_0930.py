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
    assert np.isnan(result[1])

def test_task_func_single_character():
    result = task_func("a")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], np.ndarray)
    assert result[0].size == 0
    assert np.isnan(result[1])

def test_task_func_two_characters():
    result = task_func("ab")
    expected_difference = np.array([1])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], expected_difference)
    assert result[1] == 0.0

def test_task_func_multiple_characters():
    result = task_func("abc")
    expected_difference = np.array([1, 1])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], expected_difference)
    assert result[1] == 0.0

def test_task_func_non_consecutive_characters():
    result = task_func("aeb")
    expected_difference = np.array([4, -4])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], expected_difference)
    assert result[1] > 0.0

def test_task_func_unicode_characters():
    result = task_func("😊👍")
    expected_difference = np.array([1276])
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], expected_difference)
    assert result[1] > 0.0