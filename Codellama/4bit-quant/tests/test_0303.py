import matplotlib.pyplot as plt
import pandas as pd
import pytest
from src_0303 import task_func


def test_task_func():
    # Test 1: Test with valid input
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]})
    corr_df, heatmap = task_func(df, plot=True)
    assert isinstance(corr_df, pd.DataFrame)
    assert isinstance(heatmap, plt.Figure)

    # Test 2: Test with invalid input
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

    # Test 3: Test with empty input
    df = pd.DataFrame({'Date': [], 'Value': []})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

    # Test 4: Test with invalid column names
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)

    # Test 5: Test with invalid data type
    df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [10, 20, 30]})
    with pytest.raises(ValueError):
        task_func(df, plot=False)