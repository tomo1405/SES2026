import pytest
from src_1095 import task_func

def test_task_func():
    text = "This is a test text with $dollar_prefixed_words and $$dollar_prefixed_words."
    expected_result = [('dollar_prefixed_words', 2), ('words', 1), ('test', 1), ('is', 1), ('with', 1)]
    assert task_func(text) == expected_result