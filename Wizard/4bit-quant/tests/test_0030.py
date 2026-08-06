python
import pytest
from src_0030 import task_func

def test_task_func():
    data = np.array([[1, 2, 3], [4, 5, 6]])
    encoded_data = task_func(data)
    assert isinstance(encoded_data, str)
    assert len(encoded_data) > 0