import pytest
from src_0678 import task_func
import numpy as np
import pandas as pd
from scipy.stats import linregress

def test_task_func():
    # Create a sample DataFrame
    data = {
        'var1': [1, 2, 3, 4, 5],
        'var2': [2, 4, 6, 8, 10]
    }
    df = pd.DataFrame(data)
    
    # Calculate expected results using linregress
    regression = linregress(df['var1'], df['var2'])
    expected_predictions = regression.slope * df['var1'] + regression.intercept
    
    # Call the function to be tested
    result_df = task_func(df)
    
    # Check if the 'predicted' column exists in the result DataFrame
    assert 'predicted' in result_df.columns, "The 'predicted' column is missing from the result DataFrame."
    
    # Check if the 'predicted' column values match the expected predictions
    np.testing.assert_array_almost_equal(result_df['predicted'], expected_predictions, decimal=6, err_msg="The predicted values do not match the expected values.")
    
    # Check if the original DataFrame is not modified
    assert 'predicted' not in df.columns, "The original DataFrame should not have the 'predicted' column added."

# Run the test
if __name__ == "__main__":
    pytest.main()