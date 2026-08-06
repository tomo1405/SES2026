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
    assert df['list'].dtype == object
    assert df['sum'].dtype == np.int64
    assert df['mean'].dtype == np.float64
    assert df['std'].dtype == np.float64
    assert df['mean'].mean() == pytest.approx(df['list'].mean())
    assert df['std'].std() == pytest.approx(df['list'].std())
    assert plot.kde == True