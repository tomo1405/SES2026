import pytest
from src_0961 import task_func

def test_task_func_empty_text():
    with pytest.raises(ValueError):
        task_func("")

def test_task_func_text_with_spaces():
    text = "hello world"
    expected_password = "hlelwrd"
    assert task_func(text) == expected_password

def test_task_func_text_with_digits():
    text = "hello123"
    expected_password = "hlel123"
    assert task_func(text) == expected_password

def test_task_func_text_with_special_chars():
    text = "hello!@#$%^&*()_+-="
    expected_password = "hlel!@#$%^&*()_+-="
    assert task_func(text) == expected_password

def test_task_func_text_with_mixed_chars():
    text = "hello123!@#$%^&*()_+-="
    expected_password = "hlel123!@#$%^&*()_+-="
    assert task_func(text) == expected_password

def test_task_func_text_with_seed():
    text = "hello"
    seed = 1234
    expected_password = "hlel"
    assert task_func(text, seed) == expected_password