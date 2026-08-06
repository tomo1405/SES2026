import pytest
from src_1095 import task_func

def test_task_func():
    text = "I spent $100 on groceries and $50 on gas. I also bought a new watch for $80."
    expected_output = [
        ('100', 1),
        ('50', 1),
        ('80', 1),
        (' spent', 1),
        (' gas.', 1)
    ]
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_empty_text():
    text = ""
    expected_output = []
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_no_dollar_signs():
    text = "I just ate a sandwich for lunch."
    expected_output = [
        ('just', 1),
        ('ate', 1),
        ('sandwich', 1),
        ('lunch.', 1)
    ]
    actual_output = task_func(text)
    assert actual_output == expected_output