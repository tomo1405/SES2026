import pytest
from src_0882 import task_func
import pandas as pd
import random

# Test cases for the function
def test_task_func():
    # Test case 1: Basic functionality
    data = {
        'data': ['123x', '456x', '789x', '101x']
    }
    df = pd.DataFrame(data)
    result = task_func('dummy_file.csv', column_name='data', pattern='\d+[xX]', sample_size=2)
    assert len(result) == 2

    # Add more test cases as needed

# Add more test cases as needed