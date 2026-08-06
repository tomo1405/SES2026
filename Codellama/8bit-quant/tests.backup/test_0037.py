import pytest
from src_0037 import task_func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def test_task_func_positive_values():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    with pytest.raises(ValueError):
        task_func(df)


def test_task_func_constant_data():
    df = pd.DataFrame({"A": [1, 1, 1], "B": [1, 1, 1]})
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(df)
    assert fig is None


def test_task_func_non_constant_data():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    transformed_df, fig = task_func(df)
    assert transformed_df.equals(df)
    assert fig is not None
    assert isinstance(fig, plt.Figure)