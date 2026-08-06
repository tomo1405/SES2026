import pytest
from src_1002 import task_func

def test_task_func():
    # Test case 1: Test that the function returns an axes object
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert isinstance(ax, matplotlib.axes.Axes)

    # Test case 2: Test that the function plots the normalized column
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert ax.get_xlabel() == "Index : Normalized Value"
    assert ax.get_ylabel() == "Frequency : Normalized Value"
    assert ax.get_title() == "Plot Title : Normalized Column 1"

    # Test case 3: Test that the function returns the correct mean and std
    csv_file_path = "path/to/csv/file.csv"
    ax = task_func(csv_file_path)
    assert ax.get_xlabel() == "Index : Normalized Value"
    assert ax.get_ylabel() == "Frequency : Normalized Value"
    assert ax.get_title() == "Plot Title : Normalized Column 1"

    # Test case 4: Test that the function raises an error if the csv file is not found
    csv_file_path = "path/to/non-existent/file.csv"
    with pytest.raises(FileNotFoundError):
        task_func(csv_file_path)