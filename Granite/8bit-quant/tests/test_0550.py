import base64
import pandas as pd
from src_0550 import task_func
import pytest

def test_task_func():
    # Test case 1: Test with a sample DataFrame
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    expected_output = 'SFRyaW5nOiAxOjI6MzoxOjQNCg=='
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 1 failed"

    # Test case 2: Test with an empty DataFrame
    df = pd.DataFrame()
    expected_output = ''
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 2 failed"

    # Test case 3: Test with a DataFrame containing non-string data types
    df = pd.DataFrame({'A': [1, 2.5, 3], 'B': [True, False, True]})
    expected_output = 'U2VxdWFsOiAxOjIuNTowOjM6Kg0K'
    actual_output = task_func(df)
    assert actual_output == expected_output, "Test case 3 failed"

if __name__ == "__main__":
    pytest.main()