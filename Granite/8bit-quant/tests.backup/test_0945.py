import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pytest
from src_0945 import task_func

@pytest.fixture
def input_args():
    return {
        'start_date': '2016-01-01',
        'periods': 13,
        'freq': 'WOM-2FRI',
        'seed': 0
    }

def test_task_func_output_type(input_args):
    prices_df, ax = task_func(**input_args)
    assert isinstance(prices_df, pd.DataFrame)
    assert isinstance(ax, plt.Axes)

def test_task_func_seed_argument(input_args):
    seed = input_args['seed']
    prices_df_1, _ = task_func(**input_args)
    input_args['seed'] = None
    prices_df_2, _ = task_func(**input_args)
    assert not prices_df_1.equals(prices_df_2)
    input_args['seed'] = seed
    prices_df_3, _ = task_func(**input_args)
    assert prices_df_1.equals(prices_df_3)

def test_task_func_default_arguments(monkeypatch):
    monkeypatch.setattr(np.random, 'seed', lambda x: None)
    prices_df_1, _ = task_func()
    prices_df_2, _ = task_func(seed=None)
    assert prices_df_1.equals(prices_df_2)