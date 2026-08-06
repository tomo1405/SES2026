import pytest
from src_0647 import task_func
import pandas as pd
import os

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(csv_path='./non_existent_file.csv')
    assert str(excinfo.value) == "'./non_existent_file.csv' does not exist"

def test_task_func_valid_file(tmpdir):
    # Create a temporary CSV file
    temp_dir = tmpdir.mkdir("temp")
    csv_file = temp_dir.join("data.csv")
    data = {'date': ['2020-01-01', '2021-02-02', '2022-03-03']}
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)

    # Call the function with the temporary CSV file
    result = task_func(csv_path=str(csv_file))

    # Assert the result is a Series with counts of years
    assert isinstance(result, pd.Series)
    assert len(result) == 3  # Assuming all dates are in different years
    assert result.index.min() == 2020
    assert result.index.max() == 2022
    assert result.sum() == 3  # Total number of rows in the CSV

def test_task_func_custom_date_column(tmpdir):
    # Create a temporary CSV file with a custom date column
    temp_dir = tmpdir.mkdir("temp")
    csv_file = temp_dir.join("data.csv")
    data = {'custom_date': ['2020-01-01', '2021-02-02', '2022-03-03']}
    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)

    # Call the function with the custom date column
    result = task_func(csv_path=str(csv_file), date_column='custom_date')

    # Assert the result is a Series with counts of years
    assert isinstance(result, pd.Series)
    assert len(result) == 3  # Assuming all dates are in different years
    assert result.index.min() == 2020
    assert result.index.max() == 2022
    assert result.sum() == 3  # Total number of rows in the CSV