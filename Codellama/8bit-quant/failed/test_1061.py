import pytest
from src_1061 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func_empty_df():
    df = pd.DataFrame()
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

def test_task_func_invalid_column_name():
    df = pd.DataFrame({"column_name": [1, 2, 3]})
    column_name = "invalid_column_name"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

def test_task_func_uniform_distribution():
    df = pd.DataFrame({"column_name": [1, 2, 3, 4, 5]})
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"
    assert ax.get_xlabel() == "Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xticks() == range(5)
    assert ax.get_yticks() == [1, 2, 3, 4, 5]

def test_task_func_non_uniform_distribution():
    df = pd.DataFrame({"column_name": [1, 2, 3, 4, 5, 6]})
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is not uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"
    assert ax.get_xlabel() == "Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xticks() == range(6)
    assert ax.get_yticks() == [1, 2, 3, 4, 5, 6]