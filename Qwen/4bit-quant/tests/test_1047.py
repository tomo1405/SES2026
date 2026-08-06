from datetime import datetime

import pandas as pd
import pytest
from src_1047 import task_func


def test_task_func():
    # Test with a valid date string
    date_str = "2023-01-01"
    df = task_func(date_str)
    
    # Check if the DataFrame has the correct shape
    assert df.shape == (50, 2), "DataFrame should have 50 rows and 2 columns"
    
    # Check if the 'Employee' column contains all expected employees
    assert set(df['Employee']) == set(["John", "Alice", "Bob", "Charlie", "Dave"]), "Employee column should contain all expected names"
    
    # Check if the 'Date' column contains 10 unique dates starting from the given date
    expected_dates = pd.date_range(datetime.strptime(date_str, "%Y-%m-%d"), periods=10).tolist()
    assert df['Date'].tolist() == expected_dates, "Date column should match the expected date range"

def test_task_func_invalid_date():
    # Test with an invalid date string
    date_str = "2023-13-01"
    with pytest.raises(ValueError):
        task_func(date_str)

def test_task_func_empty_employee_list():
    # Modify the EMPLOYEES list to be empty and check the behavior
    original_employees = task_func.EMPLOYEES
    task_func.EMPLOYEES = []
    
    try:
        df = task_func("2023-01-01")
        assert df.empty, "DataFrame should be empty if EMPLOYEES list is empty"
    finally:
        # Restore the original EMPLOYEES list
        task_func.EMPLOYEES = original_employees