import matplotlib.pyplot as plt
import pandas as pd
from src_0043 import task_func


def test_task_func():
    data_matrix = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})
    n_components = 2
    df, ax = task_func(data_matrix, n_components)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.shape[1] == n_components
    assert df.columns.tolist() == [f"Component {i+1}" for i in range(n_components)]
    assert df["Mean"].tolist() == [2.0, 5.0]
    assert ax.get_xlabel() == "Number of Components"
    assert ax.get_ylabel() == "Cumulative Explained Variance"