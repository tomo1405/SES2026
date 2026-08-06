import pytest
from src_0961 import task_func

def test_task_func():
    with pytest.raises(ValueError):
        task_func("")

    assert task_func("a") == "n"
    assert task_func("1") == "8"
    assert task_func("a1") == "n8"
    assert task_func("a b") == "n b"
    assert task_func("a1b") == "n1b"
    assert task_func("a 1") == "n 8"
    assert task_func("a 1b") == "n 1b"
    assert task_func("a1b2") == "n1b2"
    assert task_func("a1b2c") == "n1b2c"