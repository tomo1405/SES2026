import pandas as pd
import random
import pytest
from src_0806 import task_func

@pytest.fixture
def dictionary():
    return {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}

@pytest.mark.parametrize("item,seed,expected_output", [
    (1, 123, ([(0, 'col1'), (1, 'col1'), (2, 'col1')], 10, pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}))),
    (3, 456, ([(0, 'col3'), (1, 'col3'), (2, 'col3')], 11, pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}))),
    (5, 789, ([(0, 'col2'), (1, 'col2'), (2, 'col2')], 12, pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]})))
])
def test_task_func(dictionary, item, seed, expected_output):
    random.seed(seed)
    result = task_func(dictionary, item, seed)
    assert result == expected_output