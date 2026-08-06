import pytest
from src_1020 import task_func

def test_task_func_valid_input():
    filename = "image.png"
    from_encoding = "cp1251"
    to_encoding = "utf8"
    expected_output = "expected_output"
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding)
    assert task_func(filename, from_encoding, to_encoding) == expected_output

def test_task_func_invalid_input():
    filename = "image.png"
    from_encoding = "cp1251"
    to_encoding = "utf8"
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding)
    assert task_func(filename, from_encoding, to_encoding) == expected_output

def test_task_func_invalid_encoding():
    filename = "image.png"
    from_encoding = "cp1251"
    to_encoding = "utf8"
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding)
    assert task_func(filename, from_encoding, to_encoding) == expected_output

def test_task_func_invalid_image():
    filename = "image.png"
    from_encoding = "cp1251"
    to_encoding = "utf8"
    with pytest.raises(ValueError):
        task_func(filename, from_encoding, to_encoding)
    assert task_func(filename, from_encoding, to_encoding) == expected_output