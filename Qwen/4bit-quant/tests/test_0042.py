import pytest
from src_0042 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def test_task_func():
    # Create a sample data matrix
    data_matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Expected skewness calculation
    expected_skewness = skew(data_matrix, axis=1)
    expected_df = pd.DataFrame(expected_skewness, columns=["Skewness"])
    
    # Call the function
    result_df, ax = task_func(data_matrix)
    
    # Check if the DataFrame is correct
    pd.testing.assert_frame_equal(result_df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "Distribution of Skewness"
    assert len(ax.patches) > 0  # Ensure there are bars in the histogram

# Run the tests
if __name__ == "__main__":
    pytest.main()