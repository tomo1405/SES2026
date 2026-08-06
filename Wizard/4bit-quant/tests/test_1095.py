python
import pytest
from src_1095 import task_func

def test_task_func():
    text = "The $100,000 in cash is not enough to buy a car. I need $500,000."
    expected_output = [('cash', 1), ('buy', 1), ('car', 1), ('not', 1), ('enough', 1)]
    assert task_func(text) == expected_output