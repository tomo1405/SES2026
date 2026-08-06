import pytest
from src_0160 import task_func

def test_task_func():
    newArray = [1, 2, 3, 4, 5]
    result = task_func(newArray)
    assert result == b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\x03\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\x02\x00\x1a\x95\x1a\x00\x00\x00'