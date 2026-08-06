import pytest
from src_0208 import task_func

def test_task_func():
    input = "https://www.example.com"
    expected_output = {
        "key1": "value1",
        "key2": "value2"
    }

    assert task_func(input) == expected_output