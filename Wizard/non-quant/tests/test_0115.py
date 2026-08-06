python
import numpy as np
import pytest
from sklearn.preprocessing import MinMaxScaler
from src_0115 import task_func

def test_task_func():
    my_dict = {"array": np.array([1, 2, 3, 4, 5])}
    result = task_func(my_dict)
    assert isinstance(result['normalized_array'], np.ndarray)
    assert result['normalized_array'].shape == (5,)
    assert result['normalized_array'].min() == 0
    assert result['normalized_array'].max() == 1