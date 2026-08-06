import pytest
from src_1030 import task_func

def test_task_func():
    rows = 10
    columns = 3
    expected_column_names = [
        chr(97 + i) for i in range(columns)
    ]
    expected_data = list("abcdefghijklmnopqrstuvwxyz")
    expected_df = pd.DataFrame(expected_data, columns=expected_column_names)
    actual_df = task_func(rows, columns)
    assert actual_df.equals(expected_df)