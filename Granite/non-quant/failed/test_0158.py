import numpy as np
import pandas as pd
import seaborn as sns
import pytest
from src_0158 import task_func

def test_task_func():
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    df, ax = task_func(data)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert 'Average' in df.columns
    assert df.shape == (3, 4)
    assert ax.get_xlabel() == 'Average'