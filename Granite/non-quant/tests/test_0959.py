import random

from src_0959 import task_func


def test_task_func():
    text = "This is a sample text."
    seed = 42
    random.seed(seed)
    expected_result = "hsi sna elpmas .txet"
    actual_result = task_func(text, seed)
    assert actual_result == expected_result

def test_task_func_with_default_seed():
    text = "This is another sample text."
    expected_result = "hsi sna elpma .txet"
    actual_result = task_func(text)
    assert actual_result == expected_result

def test_task_func_with_empty_string():
    text = ""
    expected_result = ""
    actual_result = task_func(text)
    assert actual_result == expected_result