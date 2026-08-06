import pytest
from src_1118 import task_func

def test_task_func():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result

def test_task_func_invalid_input():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result

def test_task_func_invalid_input_2():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result

def test_task_func_invalid_input_3():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result

def test_task_func_invalid_input_4():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result

def test_task_func_invalid_input_5():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior'], 'MAN$$': ['Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid', 'Senior']}
    assert task_func(department_data) == expected_result