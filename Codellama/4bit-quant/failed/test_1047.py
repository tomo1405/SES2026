import pytest
from src_1047 import task_func

def test_task_func():
    # Test case 1: Check if the function returns a DataFrame with the correct columns
    date_str = "2022-01-01"
    df = task_func(date_str)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ["Employee", "Date"]

    # Test case 2: Check if the function returns a DataFrame with the correct number of rows
    assert len(df) == 10

    # Test case 3: Check if the function returns a DataFrame with the correct data
    expected_data = [
        ["John", "2022-01-01"],
        ["Alice", "2022-01-01"],
        ["Bob", "2022-01-01"],
        ["Charlie", "2022-01-01"],
        ["Dave", "2022-01-01"],
        ["John", "2022-01-02"],
        ["Alice", "2022-01-02"],
        ["Bob", "2022-01-02"],
        ["Charlie", "2022-01-02"],
        ["Dave", "2022-01-02"],
    ]
    assert df.values.tolist() == expected_data