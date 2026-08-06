import pytest
from src_0358 import task_func
import numpy as np

def test_task_func():
    x = np.linspace(-5, 5, 100)
    with pytest.raises(TypeError):
        task_func("not_a_numpy_array")
    result = task_func(x)
    assert isinstance(result, np.ndarray)
    assert result.shape == (100,)
    assert np.all(np.iscomplex(result))