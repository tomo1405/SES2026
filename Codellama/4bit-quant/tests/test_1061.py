import pytest
from src_1061 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test case 1: DataFrame is empty
    df = pd.DataFrame()
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

    # Test case 2: DataFrame has data, but column name is not in DataFrame
    df = pd.DataFrame({"column_name": [1, 2, 3]})
    column_name = "column_name_2"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

    # Test case 3: DataFrame has data, column name is in DataFrame, but all values are null
    df = pd.DataFrame({"column_name": [None, None, None]})
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

    # Test case 4: DataFrame has data, column name is in DataFrame, and all values are not null
    df = pd.DataFrame({"column_name": [1, 2, 3]})
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"
    assert ax.get_xlabel() == "Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xticks() == range(3)
    assert ax.get_yticks() == [1, 2, 3]

    # Test case 5: DataFrame has data, column name is in DataFrame, and all values are not null, but the distribution is not uniform
    df = pd.DataFrame({"column_name": [1, 2, 3, 4, 5]})
    column_name = "column_name"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is not uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"
    assert ax.get_xlabel() == "Values"
    assert ax.get_ylabel() == "Frequency"
    assert ax.get_xticks() == range(5)
    assert ax.get_yticks() == [1, 2, 3, 4, 5]