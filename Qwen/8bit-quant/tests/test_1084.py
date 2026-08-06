import pytest
from src_1084 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_missing_keys():
    with pytest.raises(ValueError, match="Input data must contain 'Salary_String' and 'Experience' keys."):
        task_func({"Salary_String": [50000, 60000], "Age": [3, 4]})

def test_task_func_empty_data():
    ax = task_func({"Salary_String": [], "Experience": []})
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_task_func_invalid_salary_conversion():
    with pytest.raises(ValueError, match="Error converting Salary_String to float."):
        task_func({"Salary_String": ["abc", "def"], "Experience": [3, 4]})

def test_task_func_valid_data():
    ax = task_func({"Salary_String": ["50,000", "60,000"], "Experience": [3, 4]})
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Normalized Salary vs Experience"
    assert ax.get_xlabel() == "Experience"
    assert ax.get_ylabel() == "Normalized Salary"

def test_task_func_plot_content():
    ax = task_func({"Salary_String": ["50,000", "60,000"], "Experience": [3, 4]})
    fig = ax.get_figure()
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    assert len(image_base64) > 0  # Ensure the plot is generated and has content