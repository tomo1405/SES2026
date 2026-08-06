import pytest
from src_0109 import task_func
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def test_task_func():
    # Test 1: Valid DataFrame
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [1, 2, 3]})
    result, ax = task_func(df)
    assert isinstance(result, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

    # Test 2: Invalid DataFrame
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, freq='W')

    # Test 3: Invalid decomposition_model
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, decomposition_model='additive')

    # Test 4: Missing or non-numeric values in 'value' column
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [1, 2, 3]})
    with pytest.raises(ValueError):
        task_func(df, freq='D', decomposition_model='multiplicative')

    # Test 5: Valid DataFrame with missing values
    df = pd.DataFrame({'group': ['A', 'B', 'C'], 'date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'value': [1, 2, 3]})
    df.loc[1, 'value'] = None
    result, ax = task_func(df, freq='D', decomposition_model='multiplicative')
    assert isinstance(result, pd.DataFrame)
    assert isinstance(ax, plt.Axes)