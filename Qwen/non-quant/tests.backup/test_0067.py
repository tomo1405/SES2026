import pytest
from src_0067 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    # Test data
    data = [
        [1, 2, 3],
        [1, 2, 4],
        [1, 3, 5],
        [2, 3, 6],
        [2, 3, 7]
    ]
    
    # Expected result
    expected_df = pd.DataFrame({
        'col1': [1, 2],
        'col2': [2, 3],
        'col3': [2, 2]
    })
    
    # Call the function
    result_df, ax = task_func(data)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True))
    
    # Check if the plot is a Seaborn AxesSubplot
    assert isinstance(ax, plt.Axes)

# Run the tests
if __name__ == "__main__":
    pytest.main()