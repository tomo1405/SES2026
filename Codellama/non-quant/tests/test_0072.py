import pytest
from src_0072 import task_func
import pandas as pd
import seaborn as sns
import numpy as np
import ast

def test_task_func():
    csv_file = "test_data.csv"
    df, plot = task_func(csv_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.histplot)
    assert df.shape[0] > 0
    assert df.shape[1] == 4
    assert df.columns.tolist() == ['list', 'sum', 'mean', 'std']
    assert df['list'].dtype == object
    assert df['sum'].dtype == np.int64
    assert df['mean'].dtype == np.float64
    assert df['std'].dtype == np.float64
    assert plot.x.dtype == np.float64
    assert plot.y.dtype == np.float64
    assert plot.x.shape[0] > 0
    assert plot.y.shape[0] > 0