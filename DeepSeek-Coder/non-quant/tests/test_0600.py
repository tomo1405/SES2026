import pytest
from src_0600 import task_func
import pandas as pd
import time

# Sample data for testing
sample_data = {
    'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']
}
sample_df = pd.DataFrame(sample_data)

def test_task_func():
    # Test case 1: Basic functionality
    result = task_func(sample_df, 'a')
    assert result is not None, "Expected a result that is not None"

    # Add more test cases as needed

# Add more test cases as needed