import pytest
from src_1084 import task_func

def test_input_data():
    # Test that the function raises an error if the input data is missing required keys
    data = {"Salary_String": "100000", "Experience": 10}
    with pytest.raises(ValueError):
        task_func(data)

def test_empty_data():
    # Test that the function handles empty data correctly
    data = {"Salary_String": "", "Experience": ""}
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_salary_conversion():
    # Test that the function raises an error if the Salary_String cannot be converted to float
    data = {"Salary_String": "invalid", "Experience": 10}
    with pytest.raises(ValueError):
        task_func(data)

def test_normalization():
    # Test that the function normalizes the Salary_Float values correctly
    data = {"Salary_String": "100000", "Experience": 10}
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert ax.get_ylim() == (0, 1)

def test_plotting():
    # Test that the function plots the data correctly
    data = {"Salary_String": "100000", "Experience": 10}
    ax = task_func(data)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    assert ax.get_ylim() == (0, 1)