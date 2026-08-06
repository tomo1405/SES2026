import pandas as pd
import seaborn as sns
import numpy as np
from src_0662 import task_func

def test_task_func():
    x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    y = [np.array([7, 8, 9]), np.array([10, 11, 12])]
    labels = ['label1', 'label2']
    
    ax, df = task_func(x, y, labels)
    
    assert isinstance(ax, sns.axisgrid.Axes)
    assert isinstance(df, pd.DataFrame)
    assert df.index.tolist() == labels
    assert df.iloc[0].tolist() == [1, 2, 3, 7]
    assert df.iloc[1].tolist() == [4, 5, 6, 10]