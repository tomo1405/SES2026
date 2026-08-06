import pytest
from src_0678 import task_func
import numpy as np
import pandas as pd
from scipy.stats import linregress

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'var1': [1, 2, 3, 4, 5], 'var2': [2, 4, 6, 8, 10]})

    # Run the function and check the output
    output = task_func(df)
    assert isinstance(output, pd.DataFrame)
    assert 'predicted' in output.columns
    assert len(output) == len(df)

    # Check that the predicted values are correct
    predictions = np.array(regression.slope) * np.array(df['var1']) + np.array(regression.intercept)
    assert np.allclose(output['predicted'], predictions)