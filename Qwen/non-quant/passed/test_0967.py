import pytest
from src_0967 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func():
    # Create a sample DataFrame
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    }
    df = pd.DataFrame(data)

    # Call the function
    result_df, fig = task_func(df)

    # Check if the returned DataFrame is correct
    expected_cumsum_data = {
        'A': [1, 3, 6],
        'B': [4, 9, 15]
    }
    expected_cumsum_df = pd.DataFrame(expected_cumsum_data)
    pd.testing.assert_frame_equal(result_df, expected_cumsum_df)

    # Check if the plot is created correctly
    # Convert the plot to a PNG image and encode it in base64
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    # Define the expected plot characteristics
    expected_title = "Cumulative Sum per Column"
    expected_xlabel = "Index"
    expected_ylabel = "Cumulative Sum"

    # Check if the plot has the correct title, xlabel, and ylabel
    assert fig.axes[0].get_title() == expected_title
    assert fig.axes[0].get_xlabel() == expected_xlabel
    assert fig.axes[0].get_ylabel() == expected_ylabel

    # Clean up
    plt.close(fig)