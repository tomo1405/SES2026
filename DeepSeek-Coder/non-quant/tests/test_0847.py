import pytest
from src_0847 import task_func
import pandas as pd
import collections

@pytest.fixture
def sample_data():
    data = [
        {'id': 1, 'value': 'A'},
        {'id': 2, 'value': 'B'},
        {'id': 3, 'value': 'A'},
        {'id': 4, 'value': 'B'},
        {'id': 5, 'value': 'A'}
    ]
    return data

@pytest.fixture
def sample_attr():
    return 'value'

def test_task_func(sample_data, sample_attr):
    result = task_func([obj for obj in sample_data], sample_attr)
    assert isinstance(result, pd.DataFrame)
    assert not result.empty
    assert 'attribute' in result.columns
    assert 'count' in result.columns