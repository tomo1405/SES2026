python
import pytest
from src_0403 import task_func

def test_task_func():
    pattern = r'\d{3}-\d{3}-\d{4}'
    result = task_func(pattern)
    assert os.path.isfile(result)
    os.remove(result)