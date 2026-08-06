import pandas as pd
import random
import pytest

from src_0463 import task_func

@pytest.mark.parametrize("num_rows", [0, 10, 100])
@pytest.mark.parametrize("categories", [["a", "b", "c", "d", "e"], ["x", "y", "z"]])
@pytest.mark.parametrize("random_seed", [42, 123, 999])
def test_task_func(num_rows, categories, random_seed):
    df, ax = task_func(num_rows, categories, random_seed)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(ax, matplotlib.axes.Axes)
    assert len(df) == num_rows
    assert len(df["Category"].unique()) <= len(categories)
    assert df["Category"].value_counts().max() <= 100