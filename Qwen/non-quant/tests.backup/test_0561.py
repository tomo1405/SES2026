import pytest
from src_0561 import task_func
import pandas as pd

def test_task_func_empty_data():
    with pytest.raises(ValueError, match="The provided data string is empty."):
        task_func("")

def test_task_func_multiple_years():
    with pytest.raises(ValueError, match="The provided data contains entries from multiple years."):
        task_func("2020-01-10,2021-02-20")

def test_task_func_valid_data():
    ax = task_func("2020-01-10,2020-02-20,2020-03-30")
    assert isinstance(ax, plt.Axes)
    expected_df = pd.DataFrame({
        'Month': ['January', 'February', 'March'],
        'Value': [10, 20, 30]
    }).set_index('Month')
    assert ax.get_title() == "Monthly Data for 2020"
    assert all(ax.get_xticklabels() == expected_df.index)

def test_task_func_single_entry():
    ax = task_func("2020-01-10")
    assert isinstance(ax, plt.Axes)
    expected_df = pd.DataFrame({
        'Month': ['January'],
        'Value': [10]
    }).set_index('Month')
    assert ax.get_title() == "Monthly Data for 2020"
    assert all(ax.get_xticklabels() == expected_df.index)