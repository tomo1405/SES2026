import pytest
import numpy as np
import pandas as pd
from src_0639 import task_func

def test_task_func():
    num_teams = 5
    num_games = 100
    scores = np.random.randint(0, 101, size=(num_teams, num_games))
    teams = ['Team' + str(i) for i in range(1, num_teams + 1)]
    games = ['Game' + str(i) for i in range(1, num_games + 1)]
    expected_df = pd.DataFrame(scores, index=teams, columns=games)
    actual_df = task_func(num_teams, num_games)
    assert actual_df.equals(expected_df)

def test_task_func_with_default_args():
    expected_df = pd.DataFrame(np.random.randint(0, 101, size=(5, 100)), index=['Team' + str(i) for i in range(1, 6)], columns=['Game' + str(i) for i in range(1, 101)])
    actual_df = task_func()
    assert actual_df.equals(expected_df)