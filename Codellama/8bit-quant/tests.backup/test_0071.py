import pytest
from src_0071 import task_func
import pandas as pd
import numpy as np

def test_task_func():
    json_file = 'test_data.json'
    with open(json_file, 'w') as file:
        file.write('{"email": "test@example.com", "list": [1, 2, 3]}')

    df, ax = task_func(json_file)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert df.shape == (1, 4)
    assert df.columns.tolist() == COLUMNS + ["sum", "mean"]
    assert df['sum'].iloc[0] == 6
    assert df['mean'].iloc[0] == 2
    assert ax.get_xlabel() == 'sum'
    assert ax.get_ylabel() == 'mean'
    assert ax.get_title() == 'Sum and Mean of List'