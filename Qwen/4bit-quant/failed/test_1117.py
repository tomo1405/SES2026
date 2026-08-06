import pytest
from src_1117 import task_func
import random
import statistics

def test_task_func_no_emp_prefix():
    input_dict = {'HR': 5, 'EMP$$': 3}
    result = task_func(input_dict)
    assert result == (0, 0, [])

def test_task_func_zero_employees():
    input_dict = {'EMP$$': 0}
    result = task_func(input_dict)
    assert result == (0, 0, [])

def test_task_func_single_employee():
    input_dict = {'EMP$$': 1}
    with patch.object(random, 'randint', return_value=40):
        result = task_func(input_dict)
        assert result == (40, 40, [40])

def test_task_func_multiple_employees():
    input_dict = {'EMP$$': 5}
    with patch.object(random, 'randint', side_effect=[25, 30, 35, 40, 45]):
        result = task_func(input_dict)
        assert result == (35, 35, [35])

def test_task_func_mode_multiple_values():
    input_dict = {'EMP$$': 6}
    with patch.object(random, 'randint', side_effect=[30, 30, 40, 40, 50, 50]):
        result = task_func(input_dict)
        assert set(result[2]) == {30, 40, 50}

def test_task_func_large_number_of_employees():
    input_dict = {'EMP$$': 100}
    result = task_func(input_dict)
    assert isinstance(result[0], float)  # Mean should be a float
    assert isinstance(result[1], float)  # Median should be a float
    assert isinstance(result[2], list)   # Mode should be a list

def test_task_func_random_ages_within_range():
    input_dict = {'EMP$$': 10}
    result = task_func(input_dict)
    assert all(AGE_RANGE[0] <= age <= AGE_RANGE[1] for age in result[2])