python
import pytest
from src_0318 import task_func

def test_task_func():
    example_str = "This is a test string [with some tags] to test the task_func function."
    expected_result = {'test': 0.16931471805599453, 'string': 0.16931471805599453, 'tags': 0.16931471805599453, 'function': 0.16931471805599453}
    assert task_func(example_str) == expected_result