python
import itertools
import numpy as np
import pytest

from src_0872 import task_func

@pytest.fixture
def data_list():
    return [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

@pytest.fixture
def file_name():
    return 'mean_values.txt'

def test_task_func(data_list, file_name):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = []
    for column in unzipped_data[1:]:
        numeric_values = [val for val in column if isinstance(val, (int, float))]
        if numeric_values:
            mean_values.append(np.nanmean(numeric_values))
        else:
            mean_values.append(np.nan)

    with open(file_name, 'w') as f:
        for i, mean_value in enumerate(mean_values, start=1):
            f.write('Position {}: {}\n'.format(i, mean_value))

    assert task_func(data_list, file_name) == mean_values