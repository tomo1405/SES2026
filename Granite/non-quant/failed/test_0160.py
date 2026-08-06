import struct
import io
import gzip
from src_0160 import task_func
import pytest

def test_task_func():
    newArray = [1.0, 2.0, 3.0]  # Replace with your desired input
    expected_output = b'\x1f\x8b\x08\x08\x9e\xe3\x59\x53\x00\x03\x63\x60\x60\x80\x00\x01\xf3\x0b\x08\x00\x00\x00'
    actual_output = task_func(newArray)
    assert actual_output == expected_output