import pytest
from src_0072 import task_func
import pandas as pd
import seaborn as sns
import numpy as np
import ast

def test_task_func():
    csv_file = 'test_data.csv'
    df, plot = task_func(csv_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.histplot)
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'std' in df.columns
    assert df['list'].dtype == object
    assert df['sum'].dtype == np.int64
    assert df['mean'].dtype == np.float64
    assert df['std'].dtype == np.float64
    assert plot.x.dtype == np.float64
    assert plot.y.dtype == np.float64
    assert plot.x.min() >= 0
    assert plot.x.max() <= 10
    assert plot.y.min() >= 0
    assert plot.y.max() <= 10