import pandas as pd
import itertools
import random
import pytest

from src_1056 import task_func

@pytest.fixture
def colors():
    return ["red", "green", "blue"]

@pytest.fixture
def states():
    return ["AL", "AK", "AZ", "AR", "CA", "CO"]

def test_task_func(colors, states):
    df = task_func(colors, states)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (min(len(colors), len(states)), 1)
    assert all(df.columns == [f"Color:State {i+1}" for i in range(1, min(len(colors), len(states)) + 1)])
    for i in range(min(len(colors), len(states))):
        assert all(df.iloc[:, i] == [f"{colors[j]}:{states[j]}" for j in range(i, len(colors), min(len(colors), len(states)))])

def test_task_func_with_invalid_inputs(colors, states):
    with pytest.raises(ValueError):
        task_func(colors, [])
    with pytest.raises(ValueError):
        task_func([], states)