import pytest
from src_0967 import task_func
import pandas as pd
import io
import matplotlib.pyplot as plt

def test_task_func():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)

    # Call the function
    result_df, fig = task_func(df)

    # Check if the result is a tuple with two elements
    assert isinstance(result_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)

    # Check if the cumulative sum DataFrame is correct
    expected_cumsum_data = {'A': [1, 3, 6], 'B': [4, 9, 15]}
    expected_cumsum_df = pd.DataFrame(expected_cumsum_data)
    pd.testing.assert_frame_equal(result_df, expected_cumsum_df)

    # Check if the plot has been created correctly
    buf = io.BytesIO()
    fig.savefig(buf)
    buf.seek(0)
    assert len(buf.getvalue()) > 0  # Ensure that the figure has been saved to the buffer