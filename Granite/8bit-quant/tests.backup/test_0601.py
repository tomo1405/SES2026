import numpy as np
import pandas as pd
from src_0601 import task_func

def test_task_func():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']})
    letter = 'b'
    expected_statistics = {'mean': 5.0, 'median': 5.0, 'mode': 5}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics

def test_task_func_with_no_matching_words():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'date', 'elderberry']})
    letter = 'z'
    expected_statistics = {'mean': np.nan, 'median': np.nan, 'mode': np.nan}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics

def test_task_func_with_empty_df():
    df = pd.DataFrame()
    letter = 'a'
    expected_statistics = {'mean': np.nan, 'median': np.nan, 'mode': np.nan}
    actual_statistics = task_func(df, letter)
    assert actual_statistics == expected_statistics