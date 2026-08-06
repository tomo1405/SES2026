import pytest
from src_0156 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    return [
        [1, 2, 3, 4, 5, 6, 7, 8],
        [8, 7, 6, 5, 4, 3, 2, 1],
        [2, 3, 4, 5, 6, 7, 8, 9]
    ]

def test_task_func_output(sample_data):
    df, ax = task_func(sample_data)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (3, 9), "DataFrame shape is incorrect"
    
    # Check if the DataFrame has the correct column names
    expected_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'Average']
    assert list(df.columns) == expected_columns, "DataFrame columns are incorrect"
    
    # Check if the 'Average' column contains the correct values
    expected_averages = [4.5, 4.5, 5.5]
    assert df['Average'].tolist() == expected_averages, "Average column values are incorrect"
    
    # Check if the plot has been created correctly
    assert isinstance(ax, plt.Axes), "Plot axis is not of type matplotlib.axes.Axes"
    assert ax.get_ylabel() == 'Average', "Y-axis label is not set to 'Average'"