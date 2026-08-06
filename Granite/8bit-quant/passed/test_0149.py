import pandas as pd
import pytest
from src_0149 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'column_name': ['cat', 'dog', 'mouse', 'cat', 'dog', 'cat', 'mouse', 'cat']
    })

def test_task_func(input_df):
    output_df = task_func(input_df, 'column_name')
    assert 'column_name' in output_df.columns
    assert output_df['column_name'].dtype == 'int64'
    assert len(output_df['column_name']) == len(input_df)

def test_task_func_with_invalid_column_name(input_df):
    with pytest.raises(KeyError):
        task_func(input_df, 'invalid_column_name')

def test_task_func_with_invalid_input_type():
    with pytest.raises(TypeError):
        task_func('not a DataFrame', 'column_name')