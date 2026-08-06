import pytest
from src_0735 import task_func

def test_task_func():
    content = "This is a sample sentence."
    expected_output = {"DT": 1, "VBZ": 1, "DT": 1, "NN": 1, "IN": 1, "DT": 1, "NN": 1, "." : 1}
    assert task_func(content) == expected_output