import pandas as pd
import pytest

from src_0599 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']
    })

def test_task_func(input_df):
    result = task_func(input_df, 'b')
    expected_result = {5: 2}
    assert result == expected_result

def test_task_func_with_empty_df(input_df):
    input_df = pd.DataFrame()
    with pytest.raises(ValueError):
        task_func(input_df, 'b')

def test_task_func_with_invalid_letter(input_df):
    with pytest.raises(ValueError):
        task_func(input_df, 'z')