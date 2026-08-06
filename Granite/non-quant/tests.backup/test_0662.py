import pandas as pd
import seaborn as sns
import numpy as np
from src_0662 import task_func

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    ax, df = task_func(x, y, LABELS)
    assert isinstance(ax, sns.axisgrid.Axes)
    assert isinstance(df, pd.DataFrame)
    assert df.index.tolist() == LABELS
    assert df.iloc[0, 0] == 1
    assert df.iloc[0, 1] == 7
    assert df.iloc[1, 0] == 2
    assert df.iloc[1, 1] == 8