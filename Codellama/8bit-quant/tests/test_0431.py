import matplotlib.pyplot as plt
import pandas as pd
from src_0431 import task_func


def test_task_func():
    df1 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature1": [10, 20, 30, 40, 50]})
    df2 = pd.DataFrame({"id": [1, 2, 3, 4, 5], "feature2": [100, 200, 300, 400, 500]})
    column1 = "feature1"
    column2 = "feature2"

    labels, ax = task_func(df1, df2, column1, column2)

    assert isinstance(labels, np.ndarray)
    assert isinstance(ax, plt.Axes)
    assert len(labels) == len(df1)
    assert len(ax.get_xlabel()) == len(column1)
    assert len(ax.get_ylabel()) == len(column2)