import numpy as np
import pandas as pd
from scipy.stats import linregress
from src_0678 import task_func
import pytest

@pytest.fixture
def input_df():
    return pd.DataFrame({
        'var1': np.random.rand(100),
        'var2': np.random.rand(100)
    })

def test_task_func(input_df):
    output_df = task_func(input_df)
    assert 'predicted' in output_df.columns
    assert len(output_df) == len(input_df)
    assert all(output_df['predicted'] == pytest.approx(
        input_df['var1'] * output_df['var1'].iloc[0] + output_df['var2'].iloc[0]))

def test_task_func_with_zero_slope(input_df):
    input_df['var1'] = 0
    output_df = task_func(input_df)
    assert all(output_df['predicted'] == pytest.approx(output_df['var2'].iloc[0]))

def test_task_func_with_zero_intercept(input_df):
    input_df['var2'] = 0
    output_df = task_func(input_df)
    assert all(output_df['predicted'] == pytest.approx(0))