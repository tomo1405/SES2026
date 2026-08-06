import pandas as pd
from collections import Counter
from src_0680 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({'A': [1, 2, 2, 3], 'B': [2, 3, 4, 4]})

def test_task_func(input_df):
    result = task_func(input_df)
    expected_result = {
        (1, 2): 2,
        (2, 3): 2,
        (3, 4): 2
    }
    assert result == expected_result