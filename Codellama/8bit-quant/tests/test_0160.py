import pytest
from src_0160 import task_func
import struct
import io
import gzip

def test_task_func():
    newArray = [1, 2, 3, 4, 5]
    expected_output = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\x02\x00\x16\x00\x00\x00'
    output = task_func(newArray)
    assert output == expected_output