import pytest
from src_0942 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    start_date = '2023-01-01'
    periods = 10
    freq = 'D'
    random_seed = 42
    
    forecast_df, ax = task_func(start_date, periods, freq, random_seed)
    
    # Check if the DataFrame has the correct shape
    assert forecast_df.shape == (periods, 1), "DataFrame does not have the expected shape"
    
    # Check if the DataFrame index is of type DatetimeIndex
    assert isinstance(forecast_df.index, pd.DatetimeIndex), "DataFrame index is not of type DatetimeIndex"
    
    # Check if the DataFrame contains the correct columns
    assert list(forecast_df.columns) == ['Sales'], "DataFrame does not contain the expected column 'Sales'"
    
    # Check if the Sales values are within the expected range
    assert all(forecast_df['Sales'] >= 100) and all(forecast_df['Sales'] <= 500), "Sales values are out of the expected range"
    
    # Check if the plot is created with the correct title and labels
    assert ax.get_title() == 'Sales Forecast', "Plot does not have the expected title"
    assert ax.get_xlabel() == 'Date', "Plot does not have the expected x-label"
    assert ax.get_ylabel() == 'Sales', "Plot does not have the expected y-label"
    
    # Check if the grid is enabled
    assert ax.gridOn, "Grid is not enabled in the plot"
    
    # Close the plot to avoid displaying it during tests
    plt.close(fig)

# Run the test
if __name__ == "__main__":
    pytest.main()