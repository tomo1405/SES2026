import pytest
from src_0601 import task_func
import numpy as np
import pandas as pd

def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elephant']})
    letter = 'a'
    expected_statistics = {'mean': 5, 'median': 5, 'mode': 5}
    assert task_func(df, letter) == expected_statistics

    letter = 'b'
    expected_statistics = {'mean': 6, 'median': 6, 'mode': 6}
    assert task_func(df, letter) == expected_statistics

    letter = 'c'
    expected_statistics = {'mean': 7, 'median': 7, 'mode': 7}
    assert task_func(df, letter) == expected_statistics

    letter = 'd'
    expected_statistics = {'mean': 4, 'median': 4, 'mode': 4}
    assert task_func(df, letter) == expected_statistics

    letter = 'e'
    expected_statistics = {'mean': 8, 'median': 8, 'mode': 8}
    assert task_func(df, letter) == expected_statistics