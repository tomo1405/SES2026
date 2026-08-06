import pytest
from src_1061 import task_func
import pandas as pd
import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        'column1': [1, 2, 2, 3, 3, 3],
        'column2': [4, 4, 4, 4, 5, 5],
        'column3': [1, 1, 2, 2, 2, 3]
    }
    return pd.DataFrame(data)

def test_empty_dataframe(sample_data):
    df = pd.DataFrame({})
    result = task_func(df, 'non_existent_column')
    assert "DataFrame is empty" in result[0]
    assert result[1] is not None

def test_no_data_in_column(sample_data):
    df = sample_data
    result = task_func(df, 'column3')
    assert "no data" in result[0].lower()
    assert result[1] is not None

def test_uniform_distribution(sample_data):
    df = sample_data
    result = task_func(df, 'column1')
    assert "uniform" in result[0].lower()
    assert result[1] is not None

def test_non_uniform_distribution(sample_data):
    df = sample_data
    result = task_func(df, 'column2')
    assert "not uniform" in result[0].lower()
    assert result[1] is not None