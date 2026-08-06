import pytest
from src_0639 import task_func

def test_task_func():
    num_teams = 5
    num_games = 100
    df = task_func(num_teams, num_games)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (num_teams, num_games)
    assert all(df.index == ['Team' + str(i) for i in range(1, num_teams + 1)])
    assert all(df.columns == ['Game' + str(i) for i in range(1, num_games + 1)])
    assert all(df.values >= 0)
    assert all(df.values <= 100)