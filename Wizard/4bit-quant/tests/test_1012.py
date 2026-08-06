python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    df = pd.read_csv(csv_file_path)
    groupby_data = df.groupby(col1_name)[col2_name].mean()

    _, ax = plt.subplots(figsize=(10, 6))
    ax.bar(groupby_data.index, groupby_data.values)
    ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")

    return ax

def test_task_func():
    # Test case 1: Test with valid input file
    csv_file_path = "data.csv"
    col1_name = "column1"
    col2_name = "column2"
    ax = task_func(csv_file_path, col1_name, col2_name)
    assert isinstance(ax, plt.Axes)

    # Test case 2: Test with invalid input file
    csv_file_path = "invalid_file.csv"
    col1_name = "column1"
    col2_name = "column2"
    with pytest.raises(FileNotFoundError):
        ax = task_func(csv_file_path, col1_name, col2_name)