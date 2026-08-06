import pandas as pd
import seaborn as sns
from src_0615 import task_func


def test_task_func():
    goals = {'Team A': 10, 'Team B': 20, 'Team C': 30, 'Team D': 40, 'Team E': 50}
    penalties = {'Team A': 5, 'Team B': 10, 'Team C': 15, 'Team D': 20, 'Team E': 25}

    df, plot = task_func(goals, penalties)

    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.PairGrid)

    assert df.shape == (5, 3)
    assert df.columns.tolist() == ['Team', 'Goals', 'Penalties']

    assert df['Team'].tolist() == ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
    assert df['Goals'].tolist() == [10, 20, 30, 40, 50]
    assert df['Penalties'].tolist() == [5, 10, 15, 20, 25]

    assert plot.axes.shape == (3, 3)
    assert plot.axes.shape == (3, 3)
    assert plot.axes.shape == (3, 3)

    assert plot.axes[0, 0].get_title() == 'Goals'
    assert plot.axes[0, 1].get_title() == 'Penalties'
    assert plot.axes[0, 2].get_title() == 'Goals'

    assert plot.axes[1, 0].get_title() == 'Goals'
    assert plot.axes[1, 1].get_title() == 'Penalties'
    assert plot.axes[1, 2].get_title() == 'Goals'

    assert plot.axes[2, 0].get_title() == 'Goals'
    assert plot.axes[2, 1].get_title() == 'Penalties'
    assert plot.axes[2, 2].get_title() == 'Goals'