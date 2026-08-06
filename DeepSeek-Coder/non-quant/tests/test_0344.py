import pytest
from src_0344 import task_func
import pandas as pd
import matplotlib.pyplot as plt

# Fixtures for testing
@pytest.fixture
def sample_data():
    data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'A', 'B'],
        'value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_data_empty():
    return pd.DataFrame()

def test_task_func_valid(sample_data):
    df = sample_data
    col = 'category'
    title = 'Test Title'
    ax = task_func(df=df, col=col, title=title)
    assert ax is not None
    plt.close()

def test_task_func_invalid_data(sample_data_empty):
    df = sample_data_empty
    col = 'non_existent_column'
    with pytest.raises(ValueError):
        task_func(df=df, col=col)

def test_task_func_no_title(sample_data):
    df = sample_data
    col = 'category'
    ax = task_func(df=df, col=col)
    assert ax is not None
    plt.close()