import pandas as pd
from random import randint, seed
from src_0812 import task_func
import pytest

@pytest.fixture
def dictionary():
    return {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}

@pytest.mark.parametrize("item, sample_size, random_seed, expected_output", [
    (1, None, None, [
        ((0, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((0, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((0, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
    ]),
    (2, 2, None, [
        ((1, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((2, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
    ]),
    (3, None, 123, [
        ((2, 'A'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((0, 'B'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
        ((1, 'C'), pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})),
    ]),
])
def test_task_func(dictionary, item, sample_size, random_seed, expected_output):
    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)
    assert positions == expected_output[0]
    assert dataframe.equals(expected_output[1])