python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df: pd.DataFrame, column_name: str) -> (str, plt.Axes):
    if df.empty or column_name not in df.columns or df[column_name].isnull().all():
        message = "The DataFrame is empty or the specified column has no data."
        _, ax = plt.subplots()
        ax.set_title(f"Distribution of values in {column_name} (No Data)")
        return message, ax

    unique_values_count = df[column_name].nunique()
    total_values = len(df[column_name])
    is_uniform = total_values % unique_values_count == 0 and all(
        df[column_name].value_counts() == total_values / unique_values_count
    )

    message = (
        "The distribution of values is uniform."
        if is_uniform
        else "The distribution of values is not uniform."
    )

    _, ax = plt.subplots()
    ax.hist(df[column_name], bins=unique_values_count, edgecolor="black", alpha=0.7)
    ax.set_xticks(range(unique_values_count))
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of values in {column_name}")

    return message, ax

def test_task_func():
    # Test case 1: Empty DataFrame
    df = pd.DataFrame()
    column_name = "column_1"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

    # Test case 2: Column with no data
    df = pd.DataFrame({"column_1": []})
    column_name = "column_1"
    message, ax = task_func(df, column_name)
    assert message == "The DataFrame is empty or the specified column has no data."
    assert ax.get_title() == f"Distribution of values in {column_name} (No Data)"

    # Test case 3: Column with unique values
    df = pd.DataFrame({"column_1": [1, 2, 3, 4, 5]})
    column_name = "column_1"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"

    # Test case 4: Column with non-uniform distribution
    df = pd.DataFrame({"column_1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    column_name = "column_1"
    message, ax = task_func(df, column_name)
    assert message == "The distribution of values is not uniform."
    assert ax.get_title() == f"Distribution of values in {column_name}"