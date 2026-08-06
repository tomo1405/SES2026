import pandas as pd
import matplotlib.pyplot as plt
import pytest
from src_1012 import task_func

@pytest.fixture
def csv_file_path():
    return "path/to/csv/file.csv"

def test_task_func(csv_file_path):
    ax = task_func(csv_file_path)
    assert isinstance(ax, plt.Axes)

def test_task_func_with_custom_col_names(csv_file_path):
    ax = task_func(csv_file_path, col1_name="custom_col1", col2_name="custom_col2")
    assert ax.get_title() == "Mean of custom_col2 Grouped by custom_col1"
    assert ax.get_xlabel() == "custom_col1"
    assert ax.get_ylabel() == "Mean of custom_col2"

def test_task_func_with_invalid_csv_file_path(csv_file_path):
    with pytest.raises(FileNotFoundError):
        task_func("invalid/csv/file/path.csv")