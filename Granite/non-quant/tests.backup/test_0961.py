import pytest
from src_0961 import task_func
import string
import random

def test_task_func():
    # Test case 1: text is empty
    with pytest.raises(ValueError) as excinfo:
        task_func("")
    assert "text cannot be empty." in str(excinfo.value)

    # Test case 2: text contains only letters
    text = "abcdefghijklmnopqrstuvwxyz"
    password = task_func(text)
    assert len(password) == len(text)
    for char in password:
        assert char in string.ascii_lowercase

    # Test case 3: text contains only digits
    text = "0123456789"
    password = task_func(text)
    assert len(password) == len(text)
    for char in password:
        assert char in string.digits

    # Test case 4: text contains letters, digits, and spaces
    text = "abcdefghijklmnopqrstuvwxyz0123456789 "
    password = task_func(text)
    assert len(password) == len(text)
    for char in password:
        if char.isalpha():
            assert char in string.ascii_lowercase
        elif char.isdigit():
            assert char in string.digits
        else:
            assert char == " "

    # Test case 5: text contains special characters
    text = "!@#$%^&*()_+{}|[]\:;'<>?,./-"
    password = task_func(text)
    assert len(password) == len(text)
    for char in password:
        if char.isalpha():
            assert char in string.ascii_lowercase
        elif char.isdigit():
            assert char in string.digits
        else:
            assert char in "!@#$%^&*()_+{}|[]\:;'<>?,./-"