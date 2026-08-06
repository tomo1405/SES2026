import matplotlib.pyplot as plt
import pandas as pd
from src_0574 import task_func


def test_task_func():
    df, ax = task_func()
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.index.tolist() == ['Mean', 'Median', 'Standard Deviation']
    assert df.columns.tolist() == ['Array1', 'Array2']
    assert df.loc['Mean', 'Array1'] >= 0 and df.loc['Mean', 'Array1'] <= 1
    assert df.loc['Median', 'Array1'] >= 0 and df.loc['Median', 'Array1'] <= 1
    assert df.loc['Standard Deviation', 'Array1'] >= 0 and df.loc['Standard Deviation', 'Array1'] <= 1
    assert df.loc['Mean', 'Array2'] >= 0 and df.loc['Mean', 'Array2'] <= 1
    assert df.loc['Median', 'Array2'] >= 0 and df.loc['Median', 'Array2'] <= 1
    assert df.loc['Standard Deviation', 'Array2'] >= 0 and df.loc['Standard Deviation', 'Array2'] <= 1