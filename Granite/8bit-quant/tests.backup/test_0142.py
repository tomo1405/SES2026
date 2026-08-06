import numpy as np
import pandas as pd
import statistics
import pytest
from src_0142 import task_func

def test_task_func_valid_input():
    rows = 10
    df, stats_dict = task_func(rows)
    assert isinstance(df, pd.DataFrame)
    assert isinstance(stats_dict, dict)
    assert len(stats_dict) == 6
    for col in df.columns:
        assert col in stats_dict
        assert isinstance(stats_dict[col], dict)
        assert 'mean' in stats_dict[col]
        assert 'median' in stats_dict[col]

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(-1)
    with pytest.raises(ValueError):
        task_func('foo')

def test_task_func_seed():
    rows = 10
    seed = 42
    df1, _ = task_func(rows, seed=seed)
    df2, _ = task_func(rows, seed=seed)
    assert df1.equals(df2)