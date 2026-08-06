import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sns


def task_func(df):
    df = df.fillna(df.mean(axis=0))
    description = df.describe()
    plots = []
    for col in df.select_dtypes(include=[np.number]).columns:
        plot = sns.displot(df[col], bins=10)
        plots.append(plot.ax)
    return description, plots

@pytest.mark.parametrize("df", [
    pd.DataFrame(np.random.rand(100, 10)),
    pd.DataFrame(np.random.randint(0, 100, size=(100, 10)))
])
def test_task_func(df):
    description, plots = task_func(df)
    assert isinstance(description, pd.DataFrame)
    assert all(isinstance(plot, plt.Axes) for plot in plots)
    assert all(plot.get_xlabel() == "value" for plot in plots)
    assert all(plot.get_ylabel() == "count" for plot in plots)