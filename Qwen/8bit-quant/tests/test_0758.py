from src_0758 import task_func
import pytest
import numpy as np
import datetime

def test_task_func():
    # Test with a simple array of strings
    input_arr = np.array(['1.2.3', '4.5.6'])
    expected_output = np.array(['3.2.1', '6.5.4'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an empty array
    input_arr = np.array([])
    expected_output = np.array([])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with a single element array
    input_arr = np.array(['7.8.9'])
    expected_output = np.array(['9.8.7'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with different lengths
    input_arr = np.array(['1.2', '3.4.5.6', '7.8.9.10.11'])
    expected_output = np.array(['2.1', '6.5.4.3', '11.10.9.8.7'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with no dots
    input_arr = np.array(['abc', 'def', 'ghi'])
    expected_output = np.array(['abc', 'def', 'ghi'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with multiple consecutive dots
    input_arr = np.array(['1..2..3', '4...5....6'])
    expected_output = np.array(['3..2..1', '6....5...4'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with leading and trailing dots
    input_arr = np.array(['.1.2.3.', '..4.5.6..'])
    expected_output = np.array(['.3.2.1.', '..6.5.4..'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with special characters
    input_arr = np.array(['!@#.$%^&*', '()_+{}|[]\\:;"\'<>,.?/'])
    expected_output = np.array(['*^%$#@!.', '/?.<>,;:\'";|][{+_)('])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with numbers and letters
    input_arr = np.array(['a1.b2.c3', 'd4.e5.f6'])
    expected_output = np.array(['c3.b2.a1', 'f6.e5.d4'])
    assert np.array_equal(task_func(input_arr), expected_output)

    # Test with an array containing strings with unicode characters
    input_arr = np.array(['á.é.í', 'ó.ú.ý'])
    expected_output = np.array(['í.é.á', 'ý.ú.ó'])
    assert np.array_equal(task_func(input_arr), expected_output)