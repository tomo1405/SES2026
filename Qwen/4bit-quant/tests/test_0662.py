import pytest
from src_0662 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Prepare test data
    x = [np.array([1, 2, 3]), np.array([4, 5, 6]), np.array([7, 8, 9])]
    y = [np.array([10, 11, 12]), np.array([13, 14, 15]), np.array([16, 17, 18])]
    labels = ['H2O', 'O2', 'CO2']

    # Call the function
    ax, df = task_func(x, y, labels)

    # Check the DataFrame
    expected_data = [
        [1, 2, 3, 10, 11, 12],
        [4, 5, 6, 13, 14, 15],
        [7, 8, 9, 16, 17, 18]
    ]
    expected_df = pd.DataFrame(expected_data, index=labels)
    pd.testing.assert_frame_equal(df, expected_df)

    # Check the Axes object
    assert isinstance(ax, plt.Axes), "The function should return a matplotlib Axes object"

    # Close the plot to prevent it from displaying
    plt.close(ax.figure)

# Run the tests
if __name__ == "__main__":
    pytest.main()