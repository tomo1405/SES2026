python
import pandas as pd
import matplotlib.pyplot as plt
import pytest

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    cumsum_df = df.cumsum()

    fig, ax = plt.subplots()
    cumsum_df.plot(kind="bar", ax=ax)
    ax.set_title("Cumulative Sum per Column")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.legend()

    return cumsum_df, fig

def test_task_func():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    cumsum_df, fig = task_func(df)

    assert isinstance(cumsum_df, pd.DataFrame)
    assert isinstance(fig, plt.Figure)