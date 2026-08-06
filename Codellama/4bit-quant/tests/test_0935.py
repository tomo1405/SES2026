import pytest
from src_0935 import task_func

def test_task_func():
    # Test case 1:
    word = "hello"
    expected_result = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(word) == expected_result

    # Test case 2:
    word = "world"
    expected_result = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(word) == expected_result

    # Test case 3:
    word = "python"
    expected_result = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(word) == expected_result

    # Test case 4:
    word = "test"
    expected_result = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(word) == expected_result

    # Test case 5:
    word = "example"
    expected_result = "5eb63bbbe01eeed093cb22bb8f5acdc3"
    assert task_func(word) == expected_result