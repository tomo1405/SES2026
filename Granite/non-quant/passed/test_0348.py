import pandas as pd
import re
import numpy as np
from src_0348 import task_func
import pytest

# Constants
PATTERN = r"([a-fA-F\d]{32})"

# Sample input data
df = pd.DataFrame({
    'column': ['abc1234567890abcdef1234567890abcdef', 'def4567890abcdef1234567890abcdefabc', 'ghi7890abcdef1234567890abcdefabc456']
})

# Expected output data
expected_output = pd.Series({
    'abc1234567890abcdef1234567890abcdef': 2,
    'def4567890abcdef1234567890abcdefabc': 2,
    'ghi7890abcdef1234567890abcdefabc456': 2
})

def test_task_func():
    # Call the function with sample input data
    output = task_func(df, 'column')

    # Assert that the output matches the expected output
    assert output.equals(expected_output)

if __name__ == '__main__':
    pytest.main()