python
import itertools
import json
import numpy as np
import pytest

from src_0251 import task_func

@pytest.fixture
def data_list():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(data_list):
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean(column) for column in unzipped_data[1:]]

    results = {'Position {}'.format(i+1): mean_value for i, mean_value in enumerate(mean_values)}
    
    with open('mean_values.json', 'w') as f:
        json.dump(results, f)

    assert task_func(data_list) == results