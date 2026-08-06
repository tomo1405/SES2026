python
import numpy as np
import pandas as pd
import pytest

def task_func(num_teams=5, num_games=100):
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    teams = ['Team' + str(i) for i in range(1, num_teams + 1)]
    games = ['Game' + str(i) for i in range(1, num_games + 1)]
    df = pd.DataFrame(scores, index=teams, columns=games)
    return df

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 100)
    assert df.index.name == 'Team'
    assert df.columns.name == 'Game'
    assert df.notna().all().all()