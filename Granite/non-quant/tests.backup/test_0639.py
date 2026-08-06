import pytest
from src_0639 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    num_teams = 5
    num_games = 100
    expected_shape = (num_teams, num_games)
    expected_index = ['Team' + str(i) for i in range(1, num_teams + 1)]
    expected_columns = ['Game' + str(i) for i in range(1, num_games + 1)]
    df = task_func(num_teams, num_games)
    assert df.shape == expected_shape
    assert df.index.tolist() == expected_index
    assert df.columns.tolist() == expected_columns