python
import pytest
from src_0498 import task_func

def test_task_func():
    # Test with default value
    assert task_func() == 'Sunday'

    # Test with custom value
    assert task_func(3) == 'Thursday'

    # Test with negative value
    with pytest.raises(ValueError):
        task_func(-1)