import pytest
from src_1124 import task_func

def test_task_func():
    myString = "https://www.example.com, https://www.example.org"
    expected_result = {
        "www.example.com": "2023-01-01",
        "www.example.org": "2023-01-02"
    }
    assert task_func(myString) == expected_result