import pytest
from src_0943 import task_func
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def test_task_func():
    # Call the function with default parameters
    sales_df, ax = task_func()
    
    # Check if the returned DataFrame has the correct shape
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.shape == (13 * 5, 3), "DataFrame should have 13 weeks * 5 categories = 65 rows"
    
    # Check if the DataFrame contains the correct columns
    expected_columns = ['Date', 'Category', 'Sales']
    assert list(sales_df.columns) == expected_columns, "DataFrame columns do not match expected columns"
    
    # Check if the Date column is of datetime type
    assert pd.api.types.is_datetime64_any_dtype(sales_df['Date']), "Date column should be of datetime type"
    
    # Check if the Category column contains the correct categories
    assert set(sales_df['Category']) == set(['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']), "Category column does not contain all expected categories"
    
    # Check if the Sales column contains integers within the expected range
    assert sales_df['Sales'].between(100, 500).all(), "Sales values are not within the expected range [100, 500]"
    
    # Check if the plot is a matplotlib Axes object
    assert isinstance(ax, plt.Axes), "Returned plot is not a matplotlib Axes object"
    
    # Check if the plot title is correct
    assert ax.get_title() == 'Category-wise Sales Trends', "Plot title does not match expected title"
    
    # Check if the plot grid is enabled
    assert ax.gridOn, "Plot grid is not enabled"

# Run the tests
if __name__ == "__main__":
    pytest.main()