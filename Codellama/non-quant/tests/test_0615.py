import pandas as pd
import seaborn as sns
from src_0615 import task_func


def test_task_func():
    goals = {'Team A': 10, 'Team B': 5, 'Team C': 8, 'Team D': 12, 'Team E': 7}
    penalties = {'Team A': 3, 'Team B': 2, 'Team C': 4, 'Team D': 1, 'Team E': 5}

    df, plot = task_func(goals, penalties)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.PairGrid)

    assert df.shape == (5, 3)
    assert df.columns.tolist() == ['Team', 'Goals', 'Penalties']
    assert df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert df['Goals'].tolist() == [10, 5, 8, 12, 7]
    assert df['Penalties'].tolist() == [3, 2, 4, 1, 5]

    assert plot.shape == (5, 5)
    assert plot.axes.shape == (5, 5)
    assert plot.axes[0, 0].get_title() == 'Team A'
    assert plot.axes[1, 0].get_title() == 'Team B'
    assert plot.axes[2, 0].get_title() == 'Team C'
    assert plot.axes[3, 0].get_title() == 'Team D'
    assert plot.axes[4, 0].get_title() == 'Team E'