import pytest
from src_1063 import task_func
import pandas as pd
from matplotlib import pyplot as plt

def test_task_func_empty_array():
    arr = pd.DataFrame()
    ax = task_func(arr)
    assert ax.get_title() == "Time Series of Row Sums"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Sum"
    assert ax.get_legend() == None

def test_task_func_non_empty_array():
    arr = pd.DataFrame([[1, 2, 3], [4, 5, 6]])
    ax = task_func(arr)
    assert ax.get_title() == "Time Series of Row Sums"
    assert ax.get_xlabel() == "Date"
    assert ax.get_ylabel() == "Sum"
    assert ax.get_legend() == None
    assert ax.get_lines()[0].get_label() == "Sum"
    assert ax.get_lines()[0].get_data() == [(1, 6), (2, 15), (3, 24)]