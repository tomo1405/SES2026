import pytest
from src_0685 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Create a sample DataFrame for testing
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [10, 20, 30, 40, 50]
    }
    df = pd.DataFrame(data)
    
    # Call the function with the sample DataFrame
    result = task_func(df=df, col='B')
    
    # Check if the column 'B' is removed
    assert 'B' not in result.columns
    
    # Check if the 'IsEvenIndex' column is added correctly
    assert 'IsEvenIndex' in result.columns
    
    # Check the values in the 'IsEvenIndex' column
    expected_even_indices = [False, True, False, True, False]
    assert all(result['IsEvenIndex'] == expected_even_indices)

# Run the test
if __name__ == "__main__":
    pytest.main()