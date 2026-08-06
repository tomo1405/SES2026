import pytest
from src_0135 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def test_task_func_with_valid_dataframe():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)

    # Redirect the plot to a BytesIO object
    fig, ax = plt.subplots()
    with BytesIO() as buf:
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.getvalue()).decode()

    # Call the function
    result_ax = task_func(df)

    # Check if the returned axis is the same as the created axis
    assert result_ax == ax

    # Check if the plot was generated correctly
    assert img_str != ''

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()

    # Test if the function raises ValueError
    with pytest.raises(ValueError):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    # Test with a list instead of a DataFrame
    data = [1, 2, 3, 4, 5]

    # Test if the function raises ValueError
    with pytest.raises(ValueError):
        task_func(data)

def test_task_func_with_custom_bins():
    # Create a sample DataFrame
    data = {'A': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)

    # Call the function with custom bins
    result_ax = task_func(df, bins=10)

    # Check if the returned axis is not None
    assert result_ax is not None