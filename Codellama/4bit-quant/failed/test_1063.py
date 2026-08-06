import pytest
from src_1063 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test for empty array
    arr = pd.DataFrame()
    ax = task_func(arr)
    assert ax.get_title() == "Time Series of Row Sums"

    # Test for non-empty array
    arr = pd.DataFrame([[1, 2], [3, 4]])
    ax = task_func(arr)
    assert ax.get_title() == "Time Series of Row Sums"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Sum"
    assert ax.get_legend() == None

    # Test for different axis
    arr = pd.DataFrame([[1, 2], [3, 4]])
    ax = task_func(arr, axis=0)
    assert ax.get_title() == "Time Series of Column Sums"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Sum"
    assert ax.get_legend() == None