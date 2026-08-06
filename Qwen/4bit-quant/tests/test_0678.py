import pytest
from src_0678 import task_func
import pandas as pd
import numpy as np
from scipy.stats import linregress

def test_task_func():
    # Create a sample DataFrame
    data = {
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    
    # Expected result after applying the task_func
    expected_slope, expected_intercept, _, _, _ = linregress(df['var1'], df['var2'])
    expected_predictions = expected_slope * df['var1'] + expected_intercept
    expected_df = df.copy()
    expected_df['predicted'] = expected_predictions
    
    # Apply the task_func
    result_df = task_func(df)
    
    # Check if the 'predicted' column is correctly calculated
    assert 'predicted' in result_df.columns, "The 'predicted' column should be present in the DataFrame."
    assert np.allclose(result_df['predicted'], expected_df['predicted']), "The 'predicted' values do not match the expected values."

    # Check if the original columns are unchanged
    assert all(result_df[col].equals(df[col]) for col in ['var1', 'var2']), "Original columns should remain unchanged."

# Run the test
if __name__ == "__main__":
    pytest.main([__file__])