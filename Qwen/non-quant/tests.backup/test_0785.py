import pytest
from src_0785 import task_func
import pandas as pd
import os

def test_task_func_output():
    n = 5
    df = task_func(n)
    assert isinstance(df, pd.DataFrame), "The output should be a pandas DataFrame"
    assert len(df) == n, f"The DataFrame should have {n} rows"

def test_task_func_columns():
    n = 5
    df = task_func(n)
    expected_columns = {'Site', 'Category', 'Response', 'Value'}
    assert set(df.columns) == expected_columns, "The DataFrame should have the correct columns"

def test_task_func_values():
    n = 5
    df = task_func(n)
    for index, row in df.iterrows():
        assert row['Site'] in ['New York Times', 'USA Today', 'Apple News', 'CNN', 'BBC'], "Site should be one of the predefined sites"
        assert row['Category'] in ['Sports', 'Technology', 'Business', 'Politics', 'Entertainment'], "Category should be one of the predefined categories"
        assert row['Response'] in ['Strongly Disagree', 'Disagree', 'Neither Agree nor Disagree', 'Agree', 'Strongly Agree'], "Response should be one of the predefined responses"
        assert isinstance(row['Value'], int) and 1 <= row['Value'] <= 5, "Value should be an integer between 1 and 5"

def test_task_func_file_creation():
    n = 5
    file_path = 'news_survey_data.csv'
    task_func(n)
    assert os.path.exists(file_path), "The CSV file should be created"
    os.remove(file_path)  # Clean up the file after the test

def test_task_func_random_seed():
    n = 5
    random_seed = 42
    df1 = task_func(n, random_seed=random_seed)
    df2 = task_func(n, random_seed=random_seed)
    assert df1.equals(df2), "DataFrames should be identical when using the same random seed"