import pandas as pd
from random import seed, choices
from src_0800 import task_func
import pytest

@pytest.fixture
def input_list():
    return [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

@pytest.mark.parametrize("num_dataframes, expected_num_dataframes", [(1, 1), (2, 2), (5, 5)])
def test_num_dataframes(input_list, num_dataframes, expected_num_dataframes):
    common_rows, dataframes = task_func(input_list, num_dataframes=num_dataframes)
    assert len(dataframes) == expected_num_dataframes

@pytest.mark.parametrize("random_seed, expected_common_rows", [(None, []), (123, [])])
def test_random_seed(input_list, random_seed, expected_common_rows):
    seed(random_seed)
    common_rows, dataframes = task_func(input_list, random_seed=random_seed)
    assert common_rows.empty

@pytest.mark.parametrize("L, expected_common_rows", [
    ([], []),
    ([['a', 'b', 'c']], []),
    ([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']], [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
])
def test_L(L, expected_common_rows):
    common_rows, dataframes = task_func(L)
    assert common_rows.values.tolist() == expected_common_rows