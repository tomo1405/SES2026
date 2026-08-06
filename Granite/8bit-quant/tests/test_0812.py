import pandas as pd
from random import randint, seed
from src_0812 import task_func
import pytest

@pytest.fixture
def dictionary():
    return {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}

@pytest.mark.parametrize("item, sample_size, random_seed, expected_output", [
    (1, None, None, [
        ((0, 'A'), (1, 'A'), (2, 'A')),
        ((0, 'B'), (1, 'B'), (2, 'B')),
        ((0, 'C'), (1, 'C'), (2, 'C'))
    ]),
    (2, 1, None, ([(1, 'B')], pd.DataFrame({'A': [1, 2, 3], 'B': [2, 5, 6], 'C': [7, 8, 9]}, index=[1]))),
    (3, None, 42, [
        ((2, 'A'), (0, 'A'), (1, 'A')),
        ((2, 'B'), (0, 'B'), (1, 'B')),
        ((2, 'C'), (0, 'C'), (1, 'C'))
    ]),
    (4, 2, 100, ([(0, 'B'), (2, 'B')], pd.DataFrame({'A': [1, 2, 3], 'B': [4, 2, 6], 'C': [7, 8, 9]}, index=[0, 2])))
])
def test_task_func(dictionary, item, sample_size, random_seed, expected_output):
    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)
    assert positions == expected_output[0]
    assert dataframe.equals(expected_output[1])