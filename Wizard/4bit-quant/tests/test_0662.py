python
import pandas as pd
import seaborn as sns
import numpy as np
import pytest

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

def task_func(x, y, labels):
    data = []

    for i in range(len(x)):
        data.append(np.concatenate((x[i], y[i])))

    df = pd.DataFrame(data, index=labels)
    ax = sns.heatmap(df, cmap='coolwarm')
    
    return ax, df

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = LABELS
    
    ax, df = task_func(x, y, labels)
    
    assert isinstance(ax, sns.axisgrid.HeatMap)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 6)
    assert df.index.tolist() == labels