python
import numpy as np
import pytest
from src_0448 import task_func

def test_task_func():
    data = np.random.rand(100, 5)
    result = task_func(data)
    assert isinstance(result, dict)
    assert "transformed_data" in result
    assert "ax" in result
    assert isinstance(result["transformed_data"], np.ndarray)
    assert result["transformed_data"].shape == (100, 2)
    assert isinstance(result["ax"], plt.Axes)