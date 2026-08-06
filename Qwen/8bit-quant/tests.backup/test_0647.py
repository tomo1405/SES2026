import pytest
from src_0647 import task_func
import pandas as pd
from dateutil.parser import parse
import os

def test_task_func_with_valid_csv(tmpdir):
    # Create a temporary directory and a CSV file within it
    csv_file_path = tmpdir.join('data.csv')
    data = {'date': ['2020-01-01', '2021-01-01', '2020-06-01']}
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

    # Call the function with the path to the temporary CSV file
    result = task_func(str(csv_file_path))

    # Check if the result is a Series object
    assert isinstance(result, pd.Series)

    # Check if the histogram contains the correct counts for each year
    expected_counts = {2020: 2, 2021: 1}
    for year, count in expected_counts.items():
        assert result.get(year) == count

def test_task_func_with_nonexistent_csv():
    # Define a path to a non-existent CSV file
    csv_file_path = './nonexistent.csv'

    # Expect a FileNotFoundError to be raised
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(csv_file_path)

    # Check if the error message contains the correct path
    assert str(csv_file_path) in str(excinfo.value)

def test_task_func_with_invalid_date_column(tmpdir):
    # Create a temporary directory and a CSV file within it
    csv_file_path = tmpdir.join('data.csv')
    data = {'invalid_date': ['2020-01-01', '2021-01-01', '2020-06-01']}
    df = pd.DataFrame(data)
    df.to_csv(csv_file_path, index=False)

    # Call the function with an invalid date column name
    with pytest.raises(KeyError) as excinfo:
        task_func(str(csv_file_path), date_column='date')

    # Check if the error message contains the correct column name
    assert 'date' in str(excinfo.value)

def test_task_func_with_empty_csv(tmpdir):
    # Create a temporary directory and an empty CSV file within it
    csv_file_path = tmpdir.join('data.csv')
    df = pd.DataFrame()
    df.to_csv(csv_file_path, index=False)

    # Call the function with the path to the empty CSV file
    result = task_func(str(csv_file_path))

    # Check if the result is a Series object
    assert isinstance(result, pd.Series)

    # Check if the histogram is empty
    assert result.empty