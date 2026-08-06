import pytest
from src_0348 import task_func
import pandas as pd
import re
import numpy as np

# Define test cases
def test_task_func():
    # Test case 1
    data = {'column1': ['a1b2c3d4e5f6', 'f1e2d3c4b5a6']}
    df = pd.DataFrame(data)
    result = task_func(df=df, column='column1')
    expected = pd.Series([2, 2], index=['a', 'b', 'c', 'd', 'e', 'f'])
    pd.testing.assert_series_equal(result, expected)

    # Add more test cases as needed

# Run the tests
if __name__ == "__main__":
    pytest.main()