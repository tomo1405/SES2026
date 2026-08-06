import pytest
from src_0293 import task_func
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def test_task_func():
    # Create a sample dataframe
    df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3],
                       'age': [20, 25, 30, 35, 40, 45],
                       'income': [50000, 60000, 70000, 80000, 90000, 100000]})

    # Test the function with the sample dataframe
    df_grouped, (hist, bins) = task_func(df)

    # Check that the output is a dataframe
    assert isinstance(df_grouped, pd.DataFrame)

    # Check that the output has the correct columns
    assert set(df_grouped.columns) == {'age', 'income'}

    # Check that the output has the correct index
    assert df_grouped.index.equals(df.index)

    # Check that the output has the correct values
    assert np.allclose(df_grouped['age'], [0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    assert np.allclose(df_grouped['income'], [0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

    # Check that the histogram is correct
    assert np.allclose(hist, [1, 1, 1, 1, 1, 1, 1, 1, 1])
    assert np.allclose(bins, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])