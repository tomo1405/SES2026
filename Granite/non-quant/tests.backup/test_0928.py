import pandas as pd
from sklearn.preprocessing import LabelEncoder
from src_0928 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'column_name': ['Hello\nWorld', 'Goodbye\nWorld', 'Foo\nBar']
    })

def test_task_func(input_df):
    output_df = task_func('path/to/file.csv', 'column_name')
    assert isinstance(output_df, pd.DataFrame)
    assert output_df.shape == input_df.shape
    assert output_df['column_name'].tolist() == [0, 1, 2]

def test_task_func_with_invalid_column_name(input_df):
    with pytest.raises(KeyError):
        task_func('path/to/file.csv', 'invalid_column_name')

def test_task_func_with_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        task_func('path/to/invalid_file.csv', 'column_name')