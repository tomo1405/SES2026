import matplotlib.pyplot as plt
import pandas as pd
from src_0574 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.index.tolist() == ['Mean', 'Median', 'Standard Deviation']
    assert df.columns.tolist() == ['Array1', 'Array2']
    assert ax.get_xlabel() == 'Statistics'
    assert ax.get_ylabel() == 'Values'