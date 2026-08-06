import pandas as pd
import seaborn as sns
import numpy as np
import ast
import pytest

from src_0072 import task_func

@pytest.fixture
def csv_file():
    return "path/to/csv/file.csv"

def test_task_func(csv_file):
    df, plot = task_func(csv_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.HistPlot)
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'std' in df.columns
    assert df['list'].apply(sum).equals(df['sum'])
    assert df['list'].apply(np.mean).equals(df['mean'])
    assert df['list'].apply(np.std).equals(df['std'])