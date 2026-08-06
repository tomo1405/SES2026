import pytest
from src_1084 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_missing_keys():
    data = {"Salary_String": ["50,000"], "Age": [30]}
    with pytest.raises(ValueError, match="Input data must contain 'Salary_String' and 'Experience' keys."):
        task_func(data)

def test_task_func_empty_data():
    data = {"Salary_String": [], "Experience": []}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_task_func_invalid_salary_conversion():
    data = {"Salary_String": ["abc"], "Experience": [3]}
    with pytest.raises(ValueError, match="Error converting Salary_String to float."):
        task_func(data)

def test_task_func_valid_data():
    data = {"Salary_String": ["50,000", "75,000"], "Experience": [3, 5]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    scatter = ax.collections[0]
    assert len(scatter.get_offsets()) == 2

def test_task_func_single_data_point():
    data = {"Salary_String": ["50,000"], "Experience": [3]}
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    scatter = ax.collections[0]
    assert len(scatter.get_offsets()) == 1