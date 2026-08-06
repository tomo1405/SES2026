import pytest
from src_0612 import task_func
import pandas as pd

@pytest.fixture
def sample_df():
    data = {
        'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12],
        'D': [13, 14, 15, 16],
        'E': [17, 18, 19, 20]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    tuples = [(1, 5), (3, 11)]
    n_plots = 2

    # Mocking plt.show to prevent actual plotting
    import matplotlib.pyplot as plt
    plt.show = lambda: None

    result_df, plot_details = task_func(sample_df, tuples, n_plots)

    # Check if the correct rows are removed
    expected_df = sample_df[(sample_df['A'] != 1) | (sample_df['B'] != 5) | (sample_df['A'] != 3) | (sample_df['C'] != 11)]
    pd.testing.assert_frame_equal(result_df, expected_df)

    # Check if the number of plots is correct
    assert len(plot_details) == min(n_plots, len(result_df))

    # Check if the columns in plot_details are valid
    for col1, col2 in plot_details:
        assert col1 in COLUMNS
        assert col2 in COLUMNS
        assert col1 != col2

# Run the test
if __name__ == "__main__":
    pytest.main()