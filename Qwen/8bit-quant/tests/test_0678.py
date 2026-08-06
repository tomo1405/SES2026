import numpy as np
import pandas as pd
import pytest
from src_0678 import task_func


@pytest.fixture
def sample_df():
    data = {
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 4, 5, 4, 5]
    }
    return pd.DataFrame(data)

def test_task_func(sample_df):
    result_df = task_func(sample_df)
    
    # Check if the 'predicted' column is added
    assert 'predicted' in result_df.columns
    
    # Check if the length of 'predicted' column matches the input DataFrame
    assert len(result_df['predicted']) == len(sample_df)
    
    # Check if the predicted values are calculated correctly
    # Using the same formula as in the task_func
    regression = linregress(sample_df['var1'], sample_df['var2'])
    expected_predictions = np.array(regression.slope) * np.array(sample_df['var1']) + np.array(regression.intercept)
    assert np.allclose(result_df['predicted'], expected_predictions)

def test_task_func_with_zero_slope(sample_df):
    # Modify the sample_df to have zero slope
    sample_df['var2'] = sample_df['var1']
    
    result_df = task_func(sample_df)
    
    # Check if the 'predicted' column is added
    assert 'predicted' in result_df.columns
    
    # Check if the length of 'predicted' column matches the input DataFrame
    assert len(result_df['predicted']) == len(sample_df)
    
    # Check if the predicted values are equal to 'var1' when slope is zero
    assert np.allclose(result_df['predicted'], sample_df['var1'])

def test_task_func_with_constant_var2(sample_df):
    # Modify the sample_df to have constant 'var2'
    sample_df['var2'] = 5
    
    result_df = task_func(sample_df)
    
    # Check if the 'predicted' column is added
    assert 'predicted' in result_df.columns
    
    # Check if the length of 'predicted' column matches the input DataFrame
    assert len(result_df['predicted']) == len(sample_df)
    
    # Check if the predicted values are equal to the intercept when 'var2' is constant
    regression = linregress(sample_df['var1'], sample_df['var2'])
    expected_predictions = np.full_like(sample_df['var1'], regression.intercept)
    assert np.allclose(result_df['predicted'], expected_predictions)