import pytest
import numpy as np
import pandas as pd
from src_0639 import task_func

def test_task_func():
    df = task_func()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 100)
    assert all(df.index == ['Team' + str(i) for i in range(1, 6)])
    assert all(df.columns == ['Game' + str(i) for i in range(1, 101)])
    scores = np.random.randint(0, 101, size=(5, 100))
    df = task_func(scores=scores)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 100)
    assert all(df.index == ['Team' + str(i) for i in range(1, 6)])
    assert all(df.columns == ['Game' + str(i) for i in range(1, 101)])
    with pytest.raises(ValueError):
        task_func(num_teams=0)
    with pytest.raises(ValueError):
        task_func(num_games=0)