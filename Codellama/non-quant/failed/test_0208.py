import pytest
from src_0208 import task_func

def test_task_func():
    input = "https://www.example.com"
    expected_output = {
        "key1": "value1",
        "key2": "value2"
    }

    output = task_func(input)

    assert output == expected_output