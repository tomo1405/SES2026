import pytest
from src_0662 import task_func
import pandas as pd
import seaborn as sns
import numpy as np

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

    ax, df = task_func(x, y, labels)

    assert isinstance(ax, sns.heatmap)
    assert isinstance(df, pd.DataFrame)
    assert df.index.tolist() == labels
    assert df.shape == (5, 6)