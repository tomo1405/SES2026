import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest

from src_1024 import task_func

@pytest.fixture
def dataframe():
    return pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100),
        'D': np.random.rand(100)
    })

def test_value_error_empty_dataframe(dataframe):
    dataframe = pd.DataFrame()
    with pytest.raises(ValueError, match="DataFrame is empty."):
        task_func(dataframe)

def test_type_error_non_numeric_columns(dataframe):
    dataframe['E'] = ['foo', 'bar', 'baz']
    with pytest.raises(TypeError, match="All columns must be numeric for correlation calculation."):
        task_func(dataframe)

def test_value_error_less_than_two_columns(dataframe):
    dataframe = pd.DataFrame({'A': np.random.rand(100)})
    with pytest.raises(ValueError, match="DataFrame must have at least two columns for correlation calculation."):
        task_func(dataframe)

def test_task_func_returns_axes_object(dataframe):
    assert isinstance(task_func(dataframe), plt.Axes)