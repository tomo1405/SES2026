import pytest
from src_0601 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elephant']})
    letter = 'a'
    expected_statistics = {'mean': 5.0, 'median': 5.0, 'mode': 5.0}
    assert task_func(df, letter) == expected_statistics

    letter = 'b'
    expected_statistics = {'mean': 6.0, 'median': 6.0, 'mode': 6.0}
    assert task_func(df, letter) == expected_statistics

    letter = 'c'
    expected_statistics = {'mean': 7.0, 'median': 7.0, 'mode': 7.0}
    assert task_func(df, letter) == expected_statistics

    letter = 'd'
    expected_statistics = {'mean': 4.0, 'median': 4.0, 'mode': 4.0}
    assert task_func(df, letter) == expected_statistics

    letter = 'e'
    expected_statistics = {'mean': 9.0, 'median': 9.0, 'mode': 9.0}
    assert task_func(df, letter) == expected_statistics