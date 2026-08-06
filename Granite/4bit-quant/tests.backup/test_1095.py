import pytest
from src_1095 import task_func

def test_task_func():
    text = "I spent $5 on groceries and $10 on gas."
    expected_output = [
        ('5', 1),
        ('10', 1),
        ('groceries', 1),
        ('gas', 1),
        ('spent', 1)
    ]
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_empty_text():
    text = ""
    expected_output = []
    actual_output = task_func(text)
    assert actual_output == expected_output

def test_task_func_with_no_dollar_prefixed_words():
    text = "This sentence has no dollar prefixed words."
    expected_output = []
    actual_output = task_func(text)
    assert actual_output == expected_output