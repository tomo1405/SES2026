import pytest
from src_0943 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    # Set the random seed to ensure reproducibility
    np.random.seed(0)
    
    # Call the function with default parameters
    sales_df, ax = task_func()
    
    # Check the DataFrame structure
    assert isinstance(sales_df, pd.DataFrame)
    assert sales_df.columns.tolist() == ['Date', 'Category', 'Sales']
    assert len(sales_df) == 13 * 5  # 13 weeks * 5 categories
    
    # Check the Date column
    expected_dates = pd.date_range(start='2016-01-01', periods=13, freq='WOM-2FRI')
    assert sales_df['Date'].tolist() == expected_dates.tolist()
    
    # Check the Category column
    expected_categories = ['Electronics', 'Fashion', 'Home & Kitchen', 'Automotive', 'Sports']
    assert sales_df['Category'].unique().tolist() == expected_categories
    
    # Check the Sales column
    sales_values = sales_df['Sales'].values
    assert all(100 <= sale < 500 for sale in sales_values)
    
    # Check the plot object
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == 'Category-wise Sales Trends'
    assert ax.grid(True)

# Run the tests
if __name__ == "__main__":
    pytest.main()