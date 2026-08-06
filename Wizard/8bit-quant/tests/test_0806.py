python
import pandas as pd
import random
import pytest

def task_func(dictionary, item, seed):
    random.seed(seed)
    random_int = random.randint(0, 9)
    df = pd.DataFrame(dictionary)
    positions = [(index, col) for col in df for index, val in enumerate(df[col]) if val == item]
    return positions, len(positions) + random_int , df

def test_task_func():
    dictionary = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    item = 5
    seed = 123
    expected_positions = [(1, 'B'), (2, 'B')]
    expected_length = 3
    expected_df = pd.DataFrame(dictionary)
    positions, length, df = task_func(dictionary, item, seed)
    assert positions == expected_positions
    assert length == expected_length
    assert df.equals(expected_df)