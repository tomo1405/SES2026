import pandas as pd
from src_0619 import task_func


def test_task_func():
    goals = 10
    penalties = 5
    results_df, plots = task_func(goals, penalties)
    assert isinstance(results_df, pd.DataFrame)
    assert len(results_df) == len(TEAMS)
    assert 'Team' in results_df.columns
    assert 'Goals' in results_df.columns
    assert 'Penalty Cost' in results_df.columns
    assert isinstance(plots, list)
    assert len(plots) == 2
    for plot in plots:
        assert isinstance(plot, sns.axisgrid.BarPlot)