import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src_0478 import task_func
import pytest

@pytest.mark.parametrize("N, seed", [(100, 42), (50, 123), (20, 456)])
def test_task_func_output_type(N, seed):
    df, ax = task_func(N, seed=seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

@pytest.mark.parametrize("N, seed", [(100, 42), (50, 123), (20, 456)])
def test_task_func_N_categories(N, seed):
    df, ax = task_func(N, seed=seed)
    assert len(df["category"].unique()) == N

@pytest.mark.parametrize("N, seed", [(100, 42), (50, 123), (20, 456)])
def test_task_func_categories_distribution(N, seed):
    df, ax = task_func(N, seed=seed)
    assert np.all(df["category"].value_counts() == N / len(df["category"].unique()))

@pytest.mark.parametrize("N, seed", [(100, 42), (50, 123), (20, 456)])
def test_task_func_scatter_plot(N, seed):
    df, ax = task_func(N, seed=seed)
    for category in df["category"].unique():
        assert len(ax.lines) == len(df["category"].unique())