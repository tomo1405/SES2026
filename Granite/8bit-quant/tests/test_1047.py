import pandas as pd
import pytest
from src_1047 import task_func


def test_task_func():
    # Test case 1: Test with valid input
    date_str = "2023-01-01"
    expected_df = pd.DataFrame([["John", "2023-01-01"], ["John", "2023-01-02"], ["John", "2023-01-03"], ["John", "2023-01-04"], ["John", "2023-01-05"], ["John", "2023-01-06"], ["John", "2023-01-07"], ["John", "2023-01-08"], ["John", "2023-01-09"], ["John", "2023-01-10"], ["Alice", "2023-01-01"], ["Alice", "2023-01-02"], ["Alice", "2023-01-03"], ["Alice", "2023-01-04"], ["Alice", "2023-01-05"], ["Alice", "2023-01-06"], ["Alice", "2023-01-07"], ["Alice", "2023-01-08"], ["Alice", "2023-01-09"], ["Alice", "2023-01-10"], ["Bob", "2023-01-01"], ["Bob", "2023-01-02"], ["Bob", "2023-01-03"], ["Bob", "2023-01-04"], ["Bob", "2023-01-05"], ["Bob", "2023-01-06"], ["Bob", "2023-01-07"], ["Bob", "2023-01-08"], ["Bob", "2023-01-09"], ["Bob", "2023-01-10"], ["Charlie", "2023-01-01"], ["Charlie", "2023-01-02"], ["Charlie", "2023-01-03"], ["Charlie", "2023-01-04"], ["Charlie", "2023-01-05"], ["Charlie", "2023-01-06"], ["Charlie", "2023-01-07"], ["Charlie", "2023-01-08"], ["Charlie", "2023-01-09"], ["Charlie", "2023-01-10"], ["Dave", "2023-01-01"], ["Dave", "2023-01-02"], ["Dave", "2023-01-03"], ["Dave", "2023-01-04"], ["Dave", "2023-01-05"], ["Dave", "2023-01-06"], ["Dave", "2023-01-07"], ["Dave", "2023-01-08"], ["Dave", "2023-01-09"], ["Dave", "2023-01-10"]], columns=["Employee", "Date"])
    actual_df = task_func(date_str)
    assert actual_df.equals(expected_df)

    # Test case 2: Test with invalid input
    date_str = "invalid_date"
    with pytest.raises(ValueError):
        task_func(date_str)