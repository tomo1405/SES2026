import pytest
from src_118 import task_func

def test_task_func():
    department_data = {'EMP$$': 10, 'MAN$$': 5, 'DEV$$': 3, 'HR$$': 2}
    expected_result = {'EMP$$': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior', 'Junior', 'Mid'], 'MAN$$': ['Junior', 'Mid', 'Senior', 'Junior', 'Mid', 'Senior'], 'DEV$$': ['Junior', 'Mid', 'Senior'], 'HR$$': ['Junior', 'Mid']}
    assert task_func(department_data) == expected_result