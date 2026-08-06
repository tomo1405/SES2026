python
import numpy as np
import pandas as pd
from scipy.stats import linregress
import pytest

def task_func(df):
    
    regression = linregress(df['var1'], df['var2'])
    
    # Explicit use of np.array to demonstrate the np. prefix usage
    # This step is purely illustrative and may not be necessary for this specific logic
    predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    
    df['predicted'] = pd.Series(predictions, index=df.index)

    return df

def test_task_func():
    df = pd.DataFrame({'var1': [1, 2, 3], 'var2': [4, 5, 6]})
    expected_df = pd.DataFrame({'var1': [1, 2, 3], 'var2': [4, 5, 6], 'predicted': [4.5, 6.5, 8.5]})
    result_df = task_func(df)
    assert result_df.equals(expected_df)