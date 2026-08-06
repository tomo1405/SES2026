import pandas as pd
import pytest
from src_1047 import task_func


def test_task_func():
    # Test case 1: Test with valid input
    date_str = "2023-01-01"
    expected_df = pd.DataFrame([["John", "2023-01-01"], ["Alice", "2023-01-01"], ["Bob", "2023-01-01"], ["Charlie", "2023-01-01"], ["Dave", "2023-01-01"]], columns=["Employee", "Date"])
    actual_df = task_func(date_str)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with invalid input
    date_str = "invalid_date"
    with pytest.raises(ValueError):
        task_func(date_str)