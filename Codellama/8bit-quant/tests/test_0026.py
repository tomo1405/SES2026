import pytest
from src_0026 import task_func

def test_task_func():
    data_dict = {"key1": "value1", "key2": "value2"}
    expected_result = "eJxLy8jNzM3NDIyMjIzNDU2Nzc3ODk6IjIwMTgtMDM6MDE6MzI6NDo="
    assert task_func(data_dict) == expected_result