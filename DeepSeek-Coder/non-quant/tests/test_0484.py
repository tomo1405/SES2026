import pytest
from src_0484 import task_func
import pandas as pd
import re

@pytest.fixture
def sample_data():
    data = {
        'column1': ['apple banana', 'banana orange', 'orange apple'],
        'column2': ['cat dog', 'dog cat', 'bird bird']
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    df = sample_data
    result = task_func(df=df, column_name='column1', pattern='a')
    assert result['column1'].tolist() == ['banana apple', 'banana orange', 'orange apple']

def test_task_func_no_pattern(sample_data):
    df = sample_data
    result = task_func(df=df, column_name='column1', pattern='')
    assert result.equals(df)

def test_task_func_no_match(sample_data):
    df = sample_data
    result = task_func(df=df, column_name='column1', pattern='z')
    assert result['column1'].tolist() == ['apple banana', 'banana orange', 'orange apple']