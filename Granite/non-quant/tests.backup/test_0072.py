import pandas as pd
import seaborn as sns
import numpy as np
import ast
import pytest

def task_func(csv_file):
    df = pd.read_csv(csv_file)
    df['list'] = df['list'].map(ast.literal_eval)
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)
    plot = sns.histplot(df['mean'], kde=True)
    return df, plot

def test_task_func():
    csv_file = "path/to/csv/file.csv"
    df, plot = task_func(csv_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.HistPlot)
    assert 'list' in df.columns
    assert 'sum' in df.columns
    assert 'mean' in df.columns
    assert 'std' in df.columns
    assert df['list'].dtype == 'object'
    assert df['sum'].dtype == 'int64'
    assert df['mean'].dtype == 'float64'
    assert df['std'].dtype == 'float64'