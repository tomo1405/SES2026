import pytest
from src_0890 import task_func

def test_task_func_valid_input():
    data_dir = "data"
    csv_file = "data.csv"
    expected_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    actual_df = task_func(data_dir, csv_file)
    assert actual_df.equals(expected_df)

def test_task_func_invalid_input():
    data_dir = "data"
    csv_file = "data.csv"
    expected_df = pd.DataFrame()
    actual_df = task_func(data_dir, csv_file)
    assert actual_df.equals(expected_df)

def test_task_func_empty_data():
    data_dir = "data"
    csv_file = "empty_data.csv"
    expected_df = pd.DataFrame()
    actual_df = task_func(data_dir, csv_file)
    assert actual_df.equals(expected_df)