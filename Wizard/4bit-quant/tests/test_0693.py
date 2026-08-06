python
import math
import pandas as pd
import pytest

def task_func(tuples_list):
    df = pd.DataFrame([(math.sin(n) for n in t) for t in tuples_list])
    return df

def test_task_func():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_df = pd.DataFrame([[math.sin(n) for n in t] for t in tuples_list])
    actual_df = task_func(tuples_list)
    assert actual_df.equals(expected_df)