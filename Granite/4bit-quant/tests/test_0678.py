import numpy as np
import pandas as pd
from scipy.stats import linregress

def task_func(df):
    
    regression = linregress(df['var1'], df['var2'])
    
    # Explicit use of np.array to demonstrate the np. prefix usage
    # This step is purely illustrative and may not be necessary for this specific logic
    predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    
    df['predicted'] = pd.Series(predictions, index=df.index)

    return df

import pytest

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 3, 4, 5, 6]
    })

    # Call the function
    result_df = task_func(df)

    # Assert the expected result
    expected_predictions = [2.0, 3.0, 4.0, 5.0, 6.0]
    assert np.array_equal(result_df['predicted'], expected_predictions)

def test_task_func_with_nan():
    # Create a sample dataframe with NaN values
    df = pd.DataFrame({
        'var1': [1, 2, np.nan, 4, 5],
        'var2': [2, 3, 4, 5, 6]
    })

    # Call the function
    result_df = task_func(df)

    # Assert the expected result
    expected_predictions = [2.0, 3.0, np.nan, 5.0, 6.0]
    assert np.array_equal(result_df['predicted'], expected_predictions)

if __name__ == "__main__":
    pytest.main()