import pandas as pd
import numpy as np
import pytest

from src_0685 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def test_task_func(input_df):
    # Test that the specified column is removed
    expected_df = input_df.drop('A', axis=1)
    actual_df = task_func(input_df, 'A')
    assert expected_df.equals(actual_df)
    
    # Test that the new column 'IsEvenIndex' is added correctly
    expected_df['IsEvenIndex'] = np.arange(len(expected_df)) % 2 == 0
    actual_df = task_func(input_df, 'A')
    assert expected_df.equals(actual_df)