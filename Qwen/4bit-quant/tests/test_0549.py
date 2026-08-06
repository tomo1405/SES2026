import base64
import random
import zlib

import pytest
from src_0549 import task_func


def test_task_func_default_length():
    result = task_func()
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_custom_length():
    result = task_func(50)
    assert isinstance(result, str)
    assert len(result) > 0

def test_task_func_reproducibility():
    random.seed(0)
    first_result = task_func(20)
    random.seed(0)
    second_result = task_func(20)
    assert first_result == second_result

def test_task_func_decoding():
    result = task_func(20)
    decoded_bytes = base64.b64decode(result)
    decompressed_string = zlib.decompress(decoded_bytes).decode('utf-8')
    assert all(c.isupper() or c.isdigit() for c in decompressed_string)
    assert len(decompressed_string) == 20

def test_task_func_edge_case_zero_length():
    with pytest.raises(ValueError):
        task_func(0)

def test_task_func_edge_case_negative_length():
    with pytest.raises(ValueError):
        task_func(-1)