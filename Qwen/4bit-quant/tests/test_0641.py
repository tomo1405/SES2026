import pandas as pd
from src_0641 import task_func


def test_task_func():
    # Call the function and capture the return value
    df = task_func()
    
    # Check if the returned object is a DataFrame
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame"
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (12, 5), "The DataFrame should have 12 rows and 5 columns"
    
    # Check if the DataFrame has the correct index and columns
    assert all(df.index == MONTHS), "The DataFrame should have the correct month indices"
    assert all(df.columns == PRODUCTS), "The DataFrame should have the correct product columns"
    
    # Check if the DataFrame contains only integers within the specified range
    assert df.min().min() >= 100, "All values in the DataFrame should be at least 100"
    assert df.max().max() <= 1000, "All values in the DataFrame should be at most 1000"

# This test will not check visualizations as they are displayed using plt.show()
# Visual tests would typically require more complex setup to capture and verify plots.