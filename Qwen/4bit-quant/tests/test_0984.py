import numpy as np
import pandas as pd
import pytest
import seaborn as sns
from src_0984 import task_func


# Mocking seaborn and numpy to avoid plotting and actual computation
class MockPairPlot:
    def savefig(self, *args, **kwargs):
        pass

sns.pairplot = lambda df: MockPairPlot()

def test_task_func_empty_dataframe():
    df = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty. Non-empty DataFrame required."):
        task_func(df)

def test_task_func_non_numeric_data():
    df = pd.DataFrame({'A': [1, 2, 'a'], 'B': [4, 5, 6]})
    with pytest.raises(TypeError, match="DataFrame contains non-numeric data. Only numeric data types are supported."):
        task_func(df)

def test_task_func_valid_input():
    df = pd.DataFrame({
        'A': np.random.randn(10),
        'B': np.random.randn(10),
        'C': np.random.randn(10)
    })
    covariance_df, pair_plot = task_func(df)
    assert isinstance(covariance_df, pd.DataFrame)
    assert isinstance(pair_plot, MockPairPlot)

def test_task_func_single_column():
    df = pd.DataFrame({'A': np.random.randn(10)})
    with pytest.raises(ValueError, match="DataFrame is empty. Non-empty DataFrame required."):
        task_func(df)

def test_task_func_all_zero_variance():
    df = pd.DataFrame({
        'A': np.zeros(10),
        'B': np.zeros(10)
    })
    covariance_df, pair_plot = task_func(df)
    assert covariance_df.equals(pd.DataFrame(np.zeros((2, 2)), index=['A', 'B'], columns=['A', 'B']))