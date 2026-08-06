import pytest
from src_1047 import task_func
from datetime import datetime
import pandas as pd

def test_task_func():
    # Test with a specific date
    date_str = "2023-01-01"
    df = task_func(date_str)
    
    # Check if the DataFrame has the correct shape
    expected_shape = (50, 2)  # 5 employees * 10 dates
    assert df.shape == expected_shape, f"Expected shape {expected_shape}, but got {df.shape}"
    
    # Check if the DataFrame contains the correct columns
    expected_columns = ["Employee", "Date"]
    assert list(df.columns) == expected_columns, f"Expected columns {expected_columns}, but got {list(df.columns)}"
    
    # Check if the 'Employee' column contains all the expected employees
    expected_employees = sorted(["John", "Alice", "Bob", "Charlie", "Dave"])
    actual_employees = sorted(df['Employee'].unique())
    assert actual_employees == expected_employees, f"Expected employees {expected_employees}, but got {actual_employees}"
    
    # Check if the 'Date' column contains the correct range of dates
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    expected_dates = pd.date_range(start_date, periods=10).tolist()
    actual_dates = df['Date'].unique().tolist()
    assert actual_dates == expected_dates, f"Expected dates {expected_dates}, but got {actual_dates}"

# Additional test cases can be added here if necessary