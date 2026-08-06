import pytest
from src_0804 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': ['a', 'b', 'c']
    }
    df = pd.DataFrame(data)
    df.to_csv('sample.csv', index=False)
    return 'sample.csv'

@pytest.fixture
def no_numeric_data():
    data = {
        'A': ['a', 'b', 'c'],
        'B': ['x', 'y', 'z']
    }
    df = pd.DataFrame(data)
    df.to_csv('no_numeric.csv', index=False)
    return 'no_numeric.csv'

def test_task_func_with_numeric_data(sample_data):
    result_df = task_func(sample_data)
    assert isinstance(result_df, pd.DataFrame)
    assert 'A' in result_df.columns
    assert 'B' in result_df.columns
    assert 'C' in result_df.columns
    assert result_df['A'].min() == 0.0
    assert result_df['A'].max() == 1.0
    assert result_df['B'].min() == 0.0
    assert result_df['B'].max() == 1.0

def test_task_func_with_no_numeric_data(no_numeric_data):
    with pytest.raises(ValueError, match="Input must at least have one numeric column."):
        task_func(no_numeric_data)