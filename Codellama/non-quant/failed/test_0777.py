import pytest
from src_0777 import task_func

def test_task_func_valid_input():
    file_path = "test_data.csv"
    output_path = "test_output.csv"
    sort_key = "title"
    linear_regression = False
    x_column = "x"
    y_column = "y"

    result = task_func(file_path, output_path, sort_key, linear_regression, x_column, y_column)

    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.read_csv(output_path))

def test_task_func_invalid_input():
    file_path = "test_data.csv"
    output_path = "test_output.csv"
    sort_key = "title"
    linear_regression = True
    x_column = "x"
    y_column = "y"

    with pytest.raises(ValueError):
        task_func(file_path, output_path, sort_key, linear_regression, x_column, y_column)