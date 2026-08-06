import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
from scipy.spatial import distance
from src_0560 import task_func


def test_task_func():
    # Test with simple arrays
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    euclidean_distance, df, ax = task_func(a, b)
    
    # Check if the Euclidean distance is calculated correctly
    expected_distance = distance.euclidean(a, b)
    assert np.isclose(euclidean_distance, expected_distance), f"Expected distance {expected_distance}, got {euclidean_distance}"
    
    # Check if the DataFrame is created correctly
    expected_df = pd.DataFrame({'A': a, 'B': b})
    pd.testing.assert_frame_equal(df, expected_df)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes), "ax should be an instance of matplotlib.axes._subplots.AxesSubplot"
    
    # Close the plot to avoid displaying it during tests
    plt.close(fig)

# Run the tests
if __name__ == "__main__":
    pytest.main()