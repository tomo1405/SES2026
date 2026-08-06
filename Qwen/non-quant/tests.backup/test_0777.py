import pytest
from src_0777 import task_func
import pandas as pd
import os

# Fixture to create a temporary CSV file
@pytest.fixture
def temp_csv_file(tmpdir):
    data = {'title': ['A', 'B', 'C'], 'value': [1, 2, 3]}
    df = pd.DataFrame(data)
    file_path = tmpdir.join('temp.csv')
    df.to_csv(file_path, index=False)
    return str(file_path)

# Test reading and sorting the CSV file
def test_task_func_read_and_sort(temp_csv_file):
    result_df = task_func(temp_csv_file, sort_key='title')
    assert isinstance(result_df, pd.DataFrame)
    assert result_df.equals(pd.DataFrame({'title': ['A', 'B', 'C'], 'value': [1, 2, 3]}))

# Test saving the sorted DataFrame to a new CSV file
def test_task_func_save_to_csv(temp_csv_file, tmpdir):
    output_path = str(tmpdir.join('output.csv'))
    task_func(temp_csv_file, output_path=output_path, sort_key='title')
    assert os.path.exists(output_path)
    saved_df = pd.read_csv(output_path)
    assert saved_df.equals(pd.DataFrame({'title': ['A', 'B', 'C'], 'value': [1, 2, 3]}))

# Test performing linear regression
def test_task_func_linear_regression(temp_csv_file):
    model = task_func(temp_csv_file, linear_regression=True, x_column='value', y_column='value')
    assert hasattr(model, 'coef_')
    assert hasattr(model, 'intercept_')

# Test error handling for missing columns in linear regression
def test_task_func_missing_columns(temp_csv_file):
    with pytest.raises(ValueError) as excinfo:
        task_func(temp_csv_file, linear_regression=True, x_column='nonexistent', y_column='value')
    assert "Specified columns for linear regression do not exist in the dataframe" in str(excinfo.value)

# Test error handling for file processing errors
def test_task_func_file_error():
    with pytest.raises(Exception) as excinfo:
        task_func('nonexistent.csv')
    assert "Error while processing the file" in str(excinfo.value)