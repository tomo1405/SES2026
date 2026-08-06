import base64
import json
import zlib
from src_0026 import task_func
import pytest

def test_task_func():
    data_dict = {"key": "value"}
    expected_result = " Compressed and encoded data"

    result = task_func(data_dict)

    assert result == expected_result