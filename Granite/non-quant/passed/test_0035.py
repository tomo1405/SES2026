import pytest
from src_0035 import task_func
def test_task_func():
    with pytest.raises(ValueError):
        task_func("")
    with pytest.raises(ValueError):
        task_func("http://example.com")
    assert task_func("Hello, world!") is not None