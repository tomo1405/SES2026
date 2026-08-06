import numpy as np
import itertools
from src_0873 import task_func
import pytest

def test_task_func():
    data_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_mean_values = [2, 5, 8]
    
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean([val for val in column if isinstance(val, (int, float))]) for column in unzipped_data]
    
    assert mean_values == expected_mean_values