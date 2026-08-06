import pytest
from src_0670 import task_func
import math
import itertools

def test_task_func_with_positive_cosines():
    input_data = {'a': math.pi/4, 'b': math.pi/3, 'c': math.pi/6}
    expected_output = ('a', 'b')
    assert task_func(input_data) == expected_output

def test_task_func_with_negative_cosines():
    input_data = {'a': 3*math.pi/4, 'b': 5*math.pi/6, 'c': 2*math.pi/3}
    expected_output = ('a', 'b')
    assert task_func(input_data) == expected_output

def test_task_func_with_mixed_cosines():
    input_data = {'a': math.pi/4, 'b': 3*math.pi/4, 'c': math.pi/6}
    expected_output = ('a', 'c')
    assert task_func(input_data) == expected_output

def test_task_func_with_single_element():
    input_data = {'a': math.pi/4}
    with pytest.raises(ValueError):  # Assuming the function raises an error for single element
        task_func(input_data)

def test_task_func_with_empty_dict():
    input_data = {}
    with pytest.raises(ValueError):  # Assuming the function raises an error for empty dictionary
        task_func(input_data)