import pytest
from src_0601 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elephant']})
    letter = 'a'
    statistics = task_func(df, letter)
    assert statistics['mean'] == 5
    assert statistics['median'] == 5
    assert statistics['mode'] == 5

    letter = 'b'
    statistics = task_func(df, letter)
    assert statistics['mean'] == 6
    assert statistics['median'] == 6
    assert statistics['mode'] == 6

    letter = 'c'
    statistics = task_func(df, letter)
    assert statistics['mean'] == 6
    assert statistics['median'] == 6
    assert statistics['mode'] == 6

    letter = 'd'
    statistics = task_func(df, letter)
    assert statistics['mean'] == 4
    assert statistics['median'] == 4
    assert statistics['mode'] == 4

    letter = 'e'
    statistics = task_func(df, letter)
    assert statistics['mean'] == 5
    assert statistics['median'] == 5
    assert statistics['mode'] == 5