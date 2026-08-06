import pytest
from src_0930 import task_func
import numpy as np
from scipy.stats import entropy

def test_task_func_empty_string():
    result = task_func("")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], np.array([]))
    assert np.isnan(result[1])

def test_task_func_single_character():
    result = task_func("a")
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert np.array_equal(result[0], np.array([]))
    assert np.isnan(result[1])

def test_task_func_two_characters():
    result = task_func("ab")
    assert isinstance(result, tuple)
    assert len(result) == 2
    expected_diff = np.array([ord('b') - ord('a')])
    assert np.array_equal(result[0], expected_diff)
    assert np.isclose(result[1], entropy(expected_diff))

def test_task_func_multiple_characters():
    result = task_func("hello")
    assert isinstance(result, tuple)
    assert len(result) == 2
    expected_diff = np.array([ord('e') - ord('h'), ord('l') - ord('e'), ord('l') - ord('l'), ord('o') - ord('l')])
    assert np.array_equal(result[0], expected_diff)
    assert np.isclose(result[1], entropy(expected_diff))

def test_task_func_non_ascii_characters():
    result = task_func("你好")
    assert isinstance(result, tuple)
    assert len(result) == 2
    expected_diff = np.array([ord('好') - ord('你')])
    assert np.array_equal(result[0], expected_diff)
    assert np.isclose(result[1], entropy(expected_diff))