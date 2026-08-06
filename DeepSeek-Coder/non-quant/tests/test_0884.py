import pytest
from src_0884 import task_func
import pandas as pd

# Sample DataFrame for testing
sample_df = pd.DataFrame({
    'column_a': [1, 2, 3, 4, 5],
    'column_b': [55, 60, 65, 70, 75],
    'column_c': [900, 900, 900, 900, 900]
})

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(sample_df, 'column_a', 'column_b', 'column_c')
    assert result is True

    # Add more test cases as needed

# Add more test cases as needed