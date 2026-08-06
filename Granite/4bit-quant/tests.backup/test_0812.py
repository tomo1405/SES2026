import pandas as pd
from random import randint, seed
from src_0812 import task_func
import pytest

@pytest.fixture
def dictionary():
    return {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}

@pytest.mark.parametrize("item, sample_size, random_seed, expected_output", [
    (1, None, None, [
        ((0, 'A'), (0, 'B'), (0, 'C')),
        ((1, 'A'), (1, 'B'), (1, 'C')),
        ((2, 'A'), (2, 'B'), (2, 'C'))
    ]),
    (2, 1, None, [
        ((1, 'B'),)
    ]),
    (3, None, 42, [
        ((2, 'C'),)
    ]),
    (4, 2, 123, [
        ((0, 'B'), (1, 'B')),
    ]),
])
def test_task_func(dictionary, item, sample_size, random_seed, expected_output):
    positions, dataframe = task_func(dictionary, item, sample_size, random_seed)
    assert positions == expected_output