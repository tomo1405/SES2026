import pytest
from src_0791 import task_func
import pandas as pd

# Assuming the function is in a module named src_0791

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)

    # Test case 1: Normal case
    result = task_func(df, 'col1', 'col2')
    assert len(result) == 5  # Since N=10 is the default, it should return all indices

    # Add more test cases as needed

if __name__ == "__main__":
    pytest.main()