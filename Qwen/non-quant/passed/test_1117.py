import pytest
from src_1117 import task_func
import random
import statistics

def test_task_func_no_emp_department():
    input_dict = {'HR': 5, 'FINANCE': 3}
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

def test_task_func_single_employee():
    input_dict = {'EMP$$1': 1}
    random.seed(42)  # Ensure reproducibility
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 42
    assert median_age == 42
    assert mode_age == [42]

def test_task_func_multiple_employees():
    input_dict = {'EMP$$1': 3, 'EMP$$2': 2}
    random.seed(42)  # Ensure reproducibility
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 42
    assert median_age == 42
    assert mode_age == [42]

def test_task_func_no_employees():
    input_dict = {'EMP$$1': 0}
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 0
    assert median_age == 0
    assert mode_age == []

def test_task_func_all_ages_same():
    input_dict = {'EMP$$1': 5}
    random.seed(42)  # Ensure reproducibility
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 42
    assert median_age == 42
    assert mode_age == [42]

def test_task_func_different_ages():
    input_dict = {'EMP$$1': 5}
    random.seed(42)  # Ensure reproducibility
    mean_age, median_age, mode_age = task_func(input_dict)
    assert mean_age == 42
    assert median_age == 42
    assert mode_age == [42]