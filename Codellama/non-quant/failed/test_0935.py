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
    expected_result = "957f0370e138e4e59ff425ca068ffadd"
    assert task_func(word) == expected_result

    # Test case 4:
    word = "testing"
    expected_result = "2079465520262678545922927871240"
    assert task_func(word) == expected_result

    # Test case 5:
    word = "engineering"
    expected_result = "68d80f13cd5e193c467791a841042a85"
    assert task_func(word) == expected_result