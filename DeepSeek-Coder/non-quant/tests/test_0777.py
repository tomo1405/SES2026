import pytest
from src_0777 import task_func
import pandas as pd
from sklearn.linear_model import LinearRegression

def test_task_func_basic():
    # Test basic functionality
    data = {
        'title': ['A', 'B', 'C'],
        'value': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    df_path = 'test_file.csv'
    df.to_csv(df_path, index=False)

    result = task_func(file_path=df_path, output_path='output.csv')
    assert result == 'output.csv'
    assert os.path.exists('output.csv')
    os.remove('output.csv')

def test_task_func_linear_regression():
    data = {
        'title': ['A', 'B', 'C'],
        'value': [1, 2, 3]
    }
    df = pd.DataFrame(data)
    df_path = 'test_file.csv'
    df.to_csv(df_path, index=False)

    result = task_func(file_path=df_path, output_path='output.csv', linear_regression=True, x_column='title', y_column='value')
    assert result == 'output.csv'
    assert os.path.exists('output.csv')
    os.remove('output.csv')

def test_task_func_invalid_columns():
    with pytest.raises(ValueError):
        task_func(file_path='invalid_path', output_path='output.csv')