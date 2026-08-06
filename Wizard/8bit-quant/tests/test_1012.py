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
    csv_file_path = "test.csv"
    col1_name = "column1"
    col2_name = "column2"

    # Test if the function returns a matplotlib axis object
    assert isinstance(task_func(csv_file_path, col1_name, col2_name), plt.Axes)

    # Test if the function returns a plot with the correct title and axis labels
    ax = task_func(csv_file_path, col1_name, col2_name)
    assert ax.get_title() == f"Mean of {col2_name} Grouped by {col1_name}"
    assert ax.get_xlabel() == col1_name
    assert ax.get_ylabel() == f"Mean of {col2_name}"

    # Test if the function raises a FileNotFoundError if the csv file is not found
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent.csv", col1_name, col2_name)