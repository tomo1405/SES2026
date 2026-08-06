import pandas as pd
import re
import numpy as np
from src_0348 import task_func

def test_task_func():
    # Create a sample DataFrame for testing
    df = pd.DataFrame({
        'column': ['abc1234567890', 'def4567890abc', 'ghi7890abcdef']
    })

    # Call the function with the sample DataFrame
    result = task_func(df, 'column')

    # Define the expected result
    expected_result = pd.Series(['abc1234567890', 'def4567890abc', 'ghi7890abcdef'], index=[0, 1, 2])

    # Assert that the result matches the expected result
    assert result.equals(expected_result)

if __name__ == '__main__':
    import pytest
    pytest.main()