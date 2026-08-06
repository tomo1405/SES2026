import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from src_0981 import task_func


def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    fig, ax = task_func(df)
    assert isinstance(fig, plt.Figure)
    assert isinstance(ax, plt.Axes)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 3)
    assert np.allclose(df.iloc[:, 0], [1, 2, 3])
    assert np.allclose(df.iloc[:, 1], [4, 5, 6])
    assert np.allclose(df.iloc[:, 2], [7, 8, 9])