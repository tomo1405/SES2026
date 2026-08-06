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

    # Check if the result is a DataFrame
    assert isinstance(result_df, pd.DataFrame)

    # Check if the cumulative sum is correct
    expected_cumsum = pd.DataFrame({'A': [1, 3, 6], 'B': [4, 9, 15]})
    pd.testing.assert_frame_equal(result_df, expected_cumsum)

    # Check if the plot is created correctly
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    assert buf.getvalue() != b''  # Ensure the buffer is not empty

    # Close the figure to avoid memory leaks
    plt.close(fig)