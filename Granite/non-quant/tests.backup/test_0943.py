import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch
from src_0943 import task_func

@patch('matplotlib.pyplot.show')
def test_task_func(mock_show):
    sales_df, ax = task_func()
    
    # Test that the returned values are of the correct type
    assert isinstance(sales_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    
    # Test that the sales DataFrame has the expected columns
    expected_columns = ['Date', 'Category', 'Sales']
    assert all(column in sales_df.columns for column in expected_columns)
    
    # Test that the plot has been displayed
    mock_show.assert_called_once()