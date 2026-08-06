import pytest
from src_0135 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_input_validation():
    with pytest.raises(ValueError):
        task_func(None)

    with pytest.raises(ValueError):
        task_func(pd.DataFrame())

def test_task_func_histogram_plot():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)

    # Capture the plot output
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

    # Call the function
    ax = task_func(df)

    # Check if the plot is created correctly
    assert ax.get_title() == 'Histogram of B'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'

    # Save the plot to a buffer and compare with the captured one
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    new_image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    assert image_base64 == new_image_base64

def test_task_func_custom_bins():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
    df = pd.DataFrame(data)

    # Call the function with custom bins
    ax = task_func(df, bins=5)

    # Check if the plot is created with the correct number of bins
    assert len(ax.patches) == 5