import pytest
from src_0776 import task_func
from string import ascii_lowercase
from collections import Counter

@pytest.mark.parametrize("string, expected_result", [
    ("abc-def", {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1}),
    ("abc-xyz", {"a": 1, "b": 1, "c": 1, "x": 1, "y": 1, "z": 1}),
    ("123-abc", {"a": 1, "b": 1, "c": 1}),
    ("abc", {"a": 1, "b": 1, "c": 1}),
    ("123", {}),
    ("xyz", {"x": 1, "y": 1, "z": 1}),
    ("", {}),
    ("-abc", {"a": 1, "b": 1, "c": 1}),
    ("abc-def-ghi", {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1, "h": 1, "i": 1}),
])
def test_task_func(string, expected_result):
    result = task_func(string)
    assert result == expected_result