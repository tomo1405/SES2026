import pytest
from src_0021 import task_func
import pandas as pd
import seaborn as sns
import ast

@pytest.fixture
def sample_data():
    data = {
        "dict_column": ['{"key1": "value1", "key2": "value2"}', '{"key3": "value3", "key4": "value4"}'],
        "hue_column": ["value1", "value2"]
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def sample_data_with_nulls():
    data = {
        "dict_column": ['{"key1": "value1", "key2": "value2"}', '{"key3": "value3", "key4": "value4"}', None],
        "hue_column": ["value1", "value2", None]
    }
    df = pd.DataFrame(data)
    return df

def test_task_func(sample_data):
    df, ax = task_func("sample_data")
    assert isinstance(df, pd.DataFrame), "The function should return a DataFrame"
    assert len(df) > 0, "The DataFrame should not be empty"
    assert "hue_column" in df.columns, "The DataFrame should have a 'hue_column' column"

def test_task_func_with_nulls(sample_data_with_nulls):
    df, ax = task_func("sample_data_with_nulls")
    assert isinstance(df, pd.DataFrame), "The function should return a DataFrame"
    assert len(df) > 0, "The DataFrame should not be empty"
    assert "hue_column" in df.columns, "The DataFrame should have a 'hue_column' column"