import pytest
from src_0608 import task_func
import pandas as pd

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3, 4, 5],
        'B': [5, 4, 3, 2, 1],
        'C': [2, 3, 4, 5, 6],
        'D': [6, 5, 4, 3, 2],
        'E': [1, 1, 1, 1, 1]
    }
    df = pd.DataFrame(data)

    # Define sample tuples for removal
    tuples = [(1, 5), (2, 4)]

    # Call the function with n_plots set to 2
    result_df, plots = task_func(df, tuples, 2)

    # Check if the DataFrame has been correctly filtered
    expected_data = {
        'A': [3, 4],
        'B': [3, 2],
        'C': [4, 5],
        'D': [5, 4],
        'E': [1, 1]
    }
    expected_df = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the number of plots is correct
    assert len(plots) == 2

    # Check if each plot is a matplotlib Axes object
    for plot in plots:
        assert isinstance(plot, plt.Axes)

# Run the tests
if __name__ == "__main__":
    pytest.main()