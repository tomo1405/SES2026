import pytest
from src_1012 import task_func

def test_task_func():
    csv_file_path = "path/to/csv/file.csv"
    col1_name = "column1"
    col2_name = "column2"

    ax = task_func(csv_file_path, col1_name, col2_name)

    assert ax.get_title() == f"Mean of {col2_name} Grouped by {col1_name}"
    assert ax.get_xlabel() == col1_name
    assert ax.get_ylabel() == f"Mean of {col2_name}"

    groupby_data = ax.get_data()
    assert groupby_data.index.name == col1_name
    assert groupby_data.values.name == col2_name

    assert groupby_data.mean() == pytest.approx(groupby_data.values.mean())