import pytest
from src_0967 import task_func
import pandas as pd
import matplotlib.pyplot as plt

def test_task_func():
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    cumsum_df, fig = task_func(df)

    assert isinstance(cumsum_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)
    assert cumsum_df.equals(pd.DataFrame({"A": [1, 3, 6], "B": [4, 9, 15]}))
    assert fig.axes[0].get_title() == "Cumulative Sum per Column"
    assert fig.axes[0].get_xlabel() == "Index"
    assert fig.axes[0].get_ylabel() == "Cumulative Sum"
    assert fig.axes[0].get_legend() == "Cumulative Sum per Column"