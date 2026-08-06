import pytest
from src_1047 import task_func
from datetime import datetime
import pandas as pd

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

def test_task_func():
    # Test with a specific date
    date_str = "2023-01-01"
    df = task_func(date_str)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (50, 2), "DataFrame should have 50 rows and 2 columns"
    
    # Check if the columns are correct
    assert list(df.columns) == ["Employee", "Date"], "Columns should be 'Employee' and 'Date'"
    
    # Check if the employees are correctly distributed
    employee_counts = df['Employee'].value_counts()
    assert all(employee_counts == 10), "Each employee should have 10 entries"
    
    # Check if the dates are correctly generated
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    expected_dates = pd.date_range(start_date, periods=10).tolist()
    assert all(df['Date'].dt.strftime("%Y-%m-%d").unique() == [d.strftime("%Y-%m-%d") for d in expected_dates]), "Dates should match the expected range"
    
    # Test with another date
    date_str = "2023-02-15"
    df = task_func(date_str)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (50, 2), "DataFrame should have 50 rows and 2 columns"
    
    # Check if the columns are correct
    assert list(df.columns) == ["Employee", "Date"], "Columns should be 'Employee' and 'Date'"
    
    # Check if the employees are correctly distributed
    employee_counts = df['Employee'].value_counts()
    assert all(employee_counts == 10), "Each employee should have 10 entries"
    
    # Check if the dates are correctly generated
    start_date = datetime.strptime(date_str, "%Y-%m-%d")
    expected_dates = pd.date_range(start_date, periods=10).tolist()
    assert all(df['Date'].dt.strftime("%Y-%m-%d").unique() == [d.strftime("%Y-%m-%d") for d in expected_dates]), "Dates should match the expected range"

# Run the tests
if __name__ == "__main__":
    pytest.main()