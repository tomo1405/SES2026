import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(data, column_name="target_column"):
    df = pd.DataFrame(data)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    if not pd.api.types.is_numeric_dtype(df[column_name]):
        df[column_name] = df[column_name].astype("category").cat.codes

    _, ax = plt.subplots()
    df[column_name].hist(ax=ax)
    ax.set_title(f"Histogram of {column_name}")
    ax.set_xlabel(column_name)
    return df, ax

def test_task_func():
    data = {'target_column': [1, 2, 3, 4, 5]}
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.columns[0] == 'target_column'
    assert ax.get_title() == 'Histogram of target_column'
    assert ax.get_xlabel() == 'target_column'