import pandas as pd
import seaborn as sns
import pytest

def task_func(data, column="c"):
    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    df = df.select_dtypes(include=["number"])

    if df.empty:
        return None

    return sns.heatmap(df.corr())

def test_task_func():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    expected_output = sns.heatmap(pd.DataFrame(data).corr())
    output = task_func(data)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_column_not_in_data():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]}
    column = "d"
    expected_output = sns.heatmap(pd.DataFrame(data).corr())
    output = task_func(data, column)
    assert output == expected_output, "Output does not match expected output"

def test_task_func_with_empty_data():
    data = {"a": [1, 2, 3], "b": [4, 5, 6], "d": [7, 8, 9]}
    expected_output = None
    output = task_func(data)
    assert output == expected_output, "Output does not match expected output"