import pytest
from src_0961 import task_func

def test_task_func():
    # Test 1: Empty text
    with pytest.raises(ValueError):
        task_func("")

    # Test 2: Text with no spaces
    assert task_func("hello") == "hello"

    # Test 3: Text with spaces
    assert task_func("hello world") == "hello world"

    # Test 4: Text with mixed characters
    assert task_func("hello123") == "hello123"

    # Test 5: Text with spaces and mixed characters
    assert task_func("hello123 world") == "hello123 world"

    # Test 6: Text with special characters
    assert task_func("hello!@#$%^&*()_+") == "hello!@#$%^&*()_+")

    # Test 7: Text with spaces and special characters
    assert task_func("hello!@#$%^&*()_+ world") == "hello!@#$%^&*()_+ world"

    # Test 8: Text with mixed characters and special characters
    assert task_func("hello123!@#$%^&*()_+") == "hello123!@#$%^&*()_+")

    # Test 9: Text with spaces, mixed characters, and special characters
    assert task_func("hello123!@#$%^&*()_+ world") == "hello123!@#$%^&*()_+ world"

    # Test 10: Text with all characters
    assert task_func("hello123!@#$%^&*()_+ world") == "hello123!@#$%^&*()_+ world"