import pandas as pd
from random import seed, choices
from src_0800 import task_func
import pytest

@pytest.fixture
def input_list():
    return [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

@pytest.mark.parametrize("num_dataframes, expected_num_dataframes", [
    (1, 1),
    (2, 2),
    (5, 5),
])
def test_num_dataframes(input_list, num_dataframes, expected_num_dataframes):
    common_rows, dataframes = task_func(input_list, num_dataframes=num_dataframes)
    assert len(dataframes) == expected_num_dataframes

@pytest.mark.parametrize("random_seed, expected_common_rows", [
    (123, pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f']], columns=['a', 'b', 'c'])),
    (456, pd.DataFrame([['g', 'h', 'i']], columns=['g', 'h', 'i'])),
])
def test_random_seed(input_list, random_seed, expected_common_rows):
    seed(random_seed)
    common_rows, dataframes = task_func(input_list)
    assert common_rows.equals(expected_common_rows)

def test_no_input(input_list):
    common_rows, dataframes = task_func([])
    assert len(dataframes) == 0
    assert common_rows.empty