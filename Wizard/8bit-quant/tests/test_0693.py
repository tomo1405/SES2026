python
import math
import pandas as pd
import pytest

def task_func(tuples_list):
    df = pd.DataFrame([(math.sin(n) for n in t) for t in tuples_list])
    return df

def test_task_func():
    tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    expected_df = pd.DataFrame([[0.8414709848078965, 0.9092974268256817, 0.1411200080598672],
                                [0.9092974268256817, 0.3420201433256687, -0.7568024953079282],
                                [-0.7568024953079282, -0.6536436208636119, -0.27941549819892586]])
    df = task_func(tuples_list)
    assert df.equals(expected_df)