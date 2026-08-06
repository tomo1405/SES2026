import pytest
from src_0723 import task_func

def test_task_func():
    url = "https://example.com/file.txt"
    expected_occurrences = 2

    result = task_func(url)

    assert result == expected_occurrences, "Expected {} occurrences, but got {}".format(expected_occurrences, result)