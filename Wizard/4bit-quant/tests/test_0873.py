python
import itertools
import numpy as np
import pytest

from src_0873 import task_func

@pytest.fixture
def data_list():
    return [
        [1, 2, 3, 4, 5],
        [1.5, 2.5, 3.5, 4.5, 5.5],
        ['a', 'b', 'c', 'd', 'e'],
        [True, False, True, False, True],
        [None, None, None, None, None],
        [1, 2, 3, None, 5],
        [1.5, 2.5, None, 4.5, 5.5],
        ['a', 'b', None, 'd', 'e'],
        [True, False, None, False, True],
        [None, None, None, None, None],
    ]

def test_task_func(data_list):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]
    assert task_func(data_list) == mean_values