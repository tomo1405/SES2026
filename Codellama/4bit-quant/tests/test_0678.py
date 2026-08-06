import numpy as np
import pandas as pd
import pytest
from src_0678 import task_func


def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'var1': [1, 2, 3, 4, 5], 'var2': [2, 4, 6, 8, 10]})

    # Test the function with the sample dataframe
    result = task_func(df)

    # Check that the resulting dataframe has the expected columns
    assert 'predicted' in result.columns

    # Check that the predicted values are correct
    expected_predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    np.testing.assert_array_equal(result['predicted'], expected_predictions)

if __name__ == '__main__':
    pytest.main()