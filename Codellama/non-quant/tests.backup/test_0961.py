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

def test_task_func_text_with_mixed_chars():
    text = "hello123 world"
    expected_password = "hlel123wrd"
    assert task_func(text) == expected_password

def test_task_func_text_with_special_chars():
    text = "hello123 world!"
    expected_password = "hlel123wrd!"
    assert task_func(text) == expected_password

def test_task_func_text_with_unicode_chars():
    text = "hello123 world😊"
    expected_password = "hlel123wrd😊"
    assert task_func(text) == expected_password

def test_task_func_text_with_non_ascii_chars():
    text = "hello123 world😊"
    expected_password = "hlel123wrd😊"
    assert task_func(text) == expected_password

def test_task_func_text_with_non_ascii_chars_and_spaces():
    text = "hello123 world😊 "
    expected_password = "hlel123wrd😊 "
    assert task_func(text) == expected_password

def test_task_func_text_with_non_ascii_chars_and_spaces_and_digits():
    text = "hello123 world😊 123"
    expected_password = "hlel123wrd😊 123"
    assert task_func(text) == expected_password

def test_task_func_text_with_non_ascii_chars_and_spaces_and_digits_and_special_chars():
    text = "hello123 world😊 123!"
    expected_password = "hlel123wrd😊 123!"
    assert task_func(text) == expected_password