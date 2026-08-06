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
    
    # Redirect matplotlib output to a BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    # Call the function
    ax = task_func(df, bins=3)
    
    # Check if the plot is created correctly
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of A'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'

def test_task_func_with_empty_dataframe():
    # Create an empty DataFrame
    df = pd.DataFrame()
    
    # Test if it raises ValueError
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func(df)

def test_task_func_with_non_dataframe_input():
    # Test with a non-DataFrame input
    input_data = [1, 2, 3, 4, 5]
    
    # Test if it raises ValueError
    with pytest.raises(ValueError, match="The input must be a non-empty pandas DataFrame."):
        task_func(input_data)

def test_task_func_with_custom_bins():
    # Create a sample DataFrame
    data = {'B': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    
    # Call the function with custom bins
    ax = task_func(df, bins=5)
    
    # Check if the plot is created correctly with custom bins
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Histogram of B'
    assert ax.get_xlabel() == 'Value'
    assert ax.get_ylabel() == 'Frequency'