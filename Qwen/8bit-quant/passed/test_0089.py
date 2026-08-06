import pytest
from src_0089 import task_func
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def test_task_func():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df, ax = task_func(start_date, end_date)

    # Check if the DataFrame has the correct number of rows
    expected_num_rows = (end_date - start_date).days + 1
    assert len(df) == expected_num_rows

    # Check if the DataFrame has the correct columns
    expected_columns = ["Date", "Sales"]
    assert list(df.columns) == expected_columns

    # Check if the 'Date' column contains the correct dates
    expected_dates = [start_date + timedelta(days=i) for i in range(expected_num_rows)]
    assert all(df['Date'] == expected_dates)

    # Check if the 'Sales' column contains values within the expected range
    assert all(0 <= sales <= 500 for sales in df['Sales'])

    # Check if the plot has the correct ylabel
    assert ax.get_ylabel() == "Sales"

# Additional test to check with different seed
def test_task_func_with_different_seed():
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 1, 5)
    df1, _ = task_func(start_date, end_date, seed=123)
    df2, _ = task_func(start_date, end_date, seed=456)

    # Check if the DataFrames are different when seeds are different
    assert not df1.equals(df2)