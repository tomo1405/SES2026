import matplotlib.pyplot as plt
import pandas as pd
from src_0431 import task_func


def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": [10, 20, 30, 40, 50], "feature2": [100, 200, 300, 400, 500]})
    df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": [10, 20, 30, 40, 50], "feature2": [100, 200, 300, 400, 500]})

    labels, ax = task_func(df1, df2)

    assert isinstance(labels, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(labels) == len(df1)
    assert len(ax.get_xlabel()) > 0
    assert len(ax.get_ylabel()) > 0
    assert len(ax.get_title()) > 0
    assert len(ax.get_legend()) > 0