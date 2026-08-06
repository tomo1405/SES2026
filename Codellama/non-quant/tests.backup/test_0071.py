import pytest
from src_0071 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    json_file = "test_data.json"
    df, ax = task_func(json_file)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (3, 4)
    assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
    assert np.allclose(df['sum'], [10, 20, 30])
    assert np.allclose(df['mean'], [10/3, 20/3, 30/3])
    assert ax.get_xlabel() == "list"
    assert ax.get_ylabel() == "sum"
    assert ax.get_title() == "Sum and Mean of List"