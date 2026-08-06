import pandas as pd
import pytest
from src_1047 import task_func


def test_task_func():
    # Test case 1: Test with valid input
    date_str = "2023-01-01"
    expected_df = pd.DataFrame([["John", "2023-01-01"], ["John", "2023-01-02"], ["John", "2023-01-03"], ["John", "2023-01-04"], ["John", "2023-01-05"], ["John", "2023-01-06"], ["John", "2023-01-07"], ["John", "2023-01-08"], ["John", "2023-01-09"], ["John", "2023-01-10"]], columns=["Employee", "Date"])
    actual_df = task_func(date_str)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with invalid input
    date_str = "2023-01-32"
    with pytest.raises(ValueError):
        task_func(date_str)