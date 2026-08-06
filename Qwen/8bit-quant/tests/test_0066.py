import pytest
from src_0066 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test data
    data = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 2, 6]
    ]
    
    # Expected DataFrame after grouping and counting unique values
    expected_df = pd.DataFrame({
        'col1': [1, 1, 2],
        'col2': [2, 3, 2],
        'col3': [2, 1, 1]
    })
    
    # Call the function
    result_df, ax = task_func(data)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))
    
    # Check if the plot has the correct labels
    assert ax.get_xlabel() == 'col1-col2'
    assert ax.get_ylabel() == 'col3'

# Run the tests
if __name__ == "__main__":
    pytest.main()