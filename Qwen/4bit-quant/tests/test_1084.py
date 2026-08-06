import matplotlib.pyplot as plt
import numpy as np
import pytest
from src_1084 import task_func


def test_task_func_missing_keys():
    with pytest.raises(ValueError, match="Input data must contain 'Salary_String' and 'Experience' keys."):
        task_func({"Salary_String": [50000], "Age": [30]})

def test_task_func_empty_data():
    ax = task_func({"Salary_String": [], "Experience": []})
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_task_func_conversion_error():
    with pytest.raises(ValueError, match="Error converting Salary_String to float."):
        task_func({"Salary_String": ["abc"], "Experience": [30]})

def test_task_func_valid_data():
    data = {
        "Salary_String": ["50,000", "60,000", "70,000"],
        "Experience": [3, 5, 7]
    }
    ax = task_func(data)
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"
    
    # Check if the plot contains the correct number of points
    lines = ax.get_lines()
    assert len(lines) == 1  # There should be one scatter plot line
    xdata, ydata = lines[0].get_data()
    assert len(xdata) == 3
    assert len(ydata) == 3

    # Check if the data is normalized
    salary_floats = np.array([50000, 60000, 70000])
    normalized_salaries = (salary_floats - salary_floats.min()) / (salary_floats.max() - salary_floats.min())
    assert np.allclose(ydata, normalized_salaries)