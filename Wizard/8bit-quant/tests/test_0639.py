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
    # Test default values
    df = task_func()
    assert df.shape == (5, 100)
    assert df.index.tolist() == ['Team1', 'Team2', 'Team3', 'Team4', 'Team5']
    assert df.columns.tolist() == ['Game' + str(i) for i in range(1, 101)]
    assert df.values.sum() == 5000

    # Test custom values
    df = task_func(num_teams=3, num_games=50)
    assert df.shape == (3, 50)
    assert df.index.tolist() == ['Team1', 'Team2', 'Team3']
    assert df.columns.tolist() == ['Game' + str(i) for i in range(1, 51)]
    assert df.values.sum() == 15000