import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
import pytest

def task_func(data_matrix):
    skewness = skew(data_matrix, axis=1)
    df = pd.DataFrame(skewness, columns=["Skewness"])
    plt.figure(figsize=(10, 5))
    df["Skewness"].plot(kind="hist", title="Distribution of Skewness")
    return df, plt.gca()

def test_task_func():
    data_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    df, ax = task_func(data_matrix)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)
    assert df.columns.tolist() == ["Skewness"]
    assert ax.get_title() == "Distribution of Skewness"