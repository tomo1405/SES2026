import pytest
from src_0156 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Sample data
    data = [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [9, 10, 11, 12, 13, 14, 15, 16]
    ]
    
    # Expected DataFrame creation
    expected_df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    expected_df['Average'] = expected_df.mean(axis=1)
    
    # Call the function
    result_df, ax = task_func(data)
    
    # Check if the DataFrame is as expected
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check if the plot has been created
    assert isinstance(ax, plt.Axes)
    assert ax.get_ylabel() == 'Average'
    
    # Check if the plot contains the correct data
    plotted_data = ax.lines[0].get_ydata()
    np.testing.assert_array_equal(plotted_data, expected_df['Average'].values)

# Run the tests
if __name__ == "__main__":
    pytest.main()