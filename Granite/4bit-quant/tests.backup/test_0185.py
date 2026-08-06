import pandas as pd
import pytest
from src_0185 import task_func

@pytest.fixture
def dataframe():
    return pd.DataFrame({
        'text_column': ['This is a test sentence.', 'Another test sentence with numbers 123 and symbols !@#$.']
    })

def test_task_func(dataframe):
    expected_result = pd.DataFrame({
        'this': [1, 1],
        'is': [1, 1],
        'a': [1, 1],
        'test': [1, 1],
        'sentence': [1, 1],
        'another': [1, 1],
        'numbers': [1, 1],
        'and': [1, 1],
        'symbols': [1, 1]
    })
    result = task_func(dataframe, 'text_column')
    assert result.equals(expected_result)

def test_task_func_with_empty_text(dataframe):
    dataframe.loc[0, 'text_column'] = ''
    expected_result = pd.DataFrame({
        'this': [0, 0],
        'is': [0, 0],
        'a': [0, 0],
        'test': [0, 0],
        'sentence': [0, 0],
        'another': [0, 0],
        'numbers': [0, 0],
        'and': [0, 0],
        'symbols': [0, 0]
    })
    result = task_func(dataframe, 'text_column')
    assert result.equals(expected_result)

def test_task_func_with_null_text(dataframe):
    dataframe.loc[0, 'text_column'] = None
    expected_result = pd.DataFrame({
        'this': [0, 0],
        'is': [0, 0],
        'a': [0, 0],
        'test': [0, 0],
        'sentence': [0, 0],
        'another': [0, 0],
        'numbers': [0, 0],
        'and': [0, 0],
        'symbols': [0, 0]
    })
    result = task_func(dataframe, 'text_column')
    assert result.equals(expected_result)