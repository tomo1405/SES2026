import pytest
from src_0935 import task_func

def test_task_func():
    # Test case 1:
    word = "hello"
    expected_result = "5d41402abc4b2a76b9719d911017c592"
    assert task_func(word) == expected_result

    # Test case 2:
    word = "world"
    expected_result = "e10adc3949ba59abbe56e057f20f883e"
    assert task_func(word) == expected_result

    # Test case 3:
    word = "python"
    expected_result = "957f037f2465e4928453864b7b33f98f"
    assert task_func(word) == expected_result