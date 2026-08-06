import base64
import json
import zlib
from src_0026 import task_func
import pytest

def test_task_func():
    data_dict = {"key": "value"}
    expected_result = "eyJrZXkiOiAidmFsdWUi fQ=="
    actual_result = task_func(data_dict)
    assert actual_result == expected_result

def test_task_func_with_invalid_input():
    data_dict = "not a dict"
    with pytest.raises(TypeError):
        task_func(data_dict)