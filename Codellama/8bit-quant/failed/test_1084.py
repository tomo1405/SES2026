import pytest
from src_1084 import task_func

def test_task_func_valid_input():
    data = {"Salary_String": ["$100,000", "$200,000", "$300,000"], "Experience": [1, 2, 3]}
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert len(ax.get_lines()) == 1

def test_task_func_invalid_input():
    data = {"Salary_String": ["$100,000", "$200,000", "$300,000"], "Experience": [1, 2, 3]}
    with pytest.raises(ValueError):
        task_func(data, "Salary_String")

def test_task_func_empty_data():
    data = {"Salary_String": [], "Experience": []}
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert len(ax.get_lines()) == 0

def test_task_func_invalid_salary_string():
    data = {"Salary_String": ["$100,000", "$200,000", "$300,000"], "Experience": [1, 2, 3]}
    with pytest.raises(ValueError):
        task_func(data, "Salary_String")