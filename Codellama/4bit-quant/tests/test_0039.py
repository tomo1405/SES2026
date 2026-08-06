import matplotlib.pyplot as plt
import pandas as pd
from src_0039 import task_func


def test_task_func():
    data_matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape == (2, 6)
    assert df.columns.tolist() == FEATURE_NAMES + ["Mean"]
    assert df["Mean"].tolist() == [3.5, 8.5]
    assert ax.get_title() == "Distribution of Means"
    assert ax.get_xlabel() == "Mean"
    assert ax.get_ylabel() == "Count"
    assert ax.get_xlim() == (0, 10)
    assert ax.get_ylim() == (0, 2)