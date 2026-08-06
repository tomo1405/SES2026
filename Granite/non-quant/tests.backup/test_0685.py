import pandas as pd
import numpy as np
import pytest

from src_0685 import task_func

@pytest.fixture
def input_df():
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

def test_task_func(input_df):
    # Test that the specified column is removed
    output_df = task_func(input_df, 'A')
    assert 'A' not in output_df.columns
    
    # Test that the new column 'IsEvenIndex' is added
    assert 'IsEvenIndex' in output_df.columns
    
    # Test that the values in 'IsEvenIndex' are correct
    expected_values = [True, False, True]
    assert (output_df['IsEvenIndex'] == expected_values).all()