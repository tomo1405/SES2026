import pytest
from src_0758 import task_func
import numpy as np

def test_task_func():
    # Test with a simple array of strings
    input_array = np.array(['1.2.3', '4.5.6', '7.8.9'])
    expected_output = np.array(['3.2.1', '6.5.4', '9.8.7'])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with an empty array
    input_array = np.array([])
    expected_output = np.array([])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with a single element array
    input_array = np.array(['10.20.30'])
    expected_output = np.array(['30.20.10'])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with strings that have different numbers of segments
    input_array = np.array(['1.2', '3.4.5', '6.7.8.9'])
    expected_output = np.array(['2.1', '5.4.3', '9.8.7.6'])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with strings that have no segments
    input_array = np.array(['1', '2', '3'])
    expected_output = np.array(['1', '2', '3'])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with strings that have only one segment
    input_array = np.array(['1.', '2.', '3.'])
    expected_output = np.array(['1.', '2.', '3.'])
    assert np.array_equal(task_func(input_array), expected_output)

    # Test with strings that have special characters
    input_array = np.array(['a.b.c', 'd.e.f!', 'g.h.i@'])
    expected_output = np.array(['c.b.a', 'f!.e.d', '@i.h.g'])
    assert np.array_equal(task_func(input_array), expected_output)