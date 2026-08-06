python
import pytest
from src_1095 import task_func

def test_task_func():
    text = "$$hello $world $$$$hi $$$$world $$$$"
    expected_output = [('hello', 1), ('world', 2), ('hi', 2), ('world', 1)]
    assert task_func(text) == expected_output