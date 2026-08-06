import pandas as pd
import seaborn as sns
import pytest

from src_0615 import task_func

goals = {'Team A': 3, 'Team B': 2, 'Team C': 1, 'Team D': 5, 'Team E': 4}
penalties = {'Team A': 1, 'Team B': 2, 'Team C': 3, 'Team D': 2, 'Team E': 1}

def test_task_func():
    df, plot = task_func(goals, penalties)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(plot, sns.axisgrid.PairGrid)

def test_task_func_with_invalid_inputs():
    with pytest.raises(ValueError):
        task_func({}, {})