import pytest
from src_0520 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    data = {'apple': [1, 2, 3], 'banana': [4, 5, 6], 'orange': [7, 8, 9]}
    expected_df = pd.DataFrame(data)
    expected_df.fillna(0, inplace=True)
    expected_fruits = ['apple', 'banana', 'orange']
    expected_labels = ['apple', 'banana', 'orange']
    expected_xlabel = "Time"
    expected_ylabel = "Sales Quantity"
    expected_title = "Fruit Sales over Time"

    actual_ax = task_func(data)
    actual_df = actual_ax.data
    actual_fruits = actual_ax.get_legend_handles_labels()[1]
    actual_xlabel = actual_ax.get_xlabel()
    actual_ylabel = actual_ax.get_ylabel()
    actual_title = actual_ax.get_title()

    assert actual_df.equals(expected_df)
    assert actual_fruits == expected_fruits
    assert actual_xlabel == expected_xlabel
    assert actual_ylabel == expected_ylabel
    assert actual_title == expected_title