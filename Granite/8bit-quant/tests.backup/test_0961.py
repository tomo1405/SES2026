import pytest
from src_0961 import task_func

def test_task_func():
    # Test case 1: text is empty
    with pytest.raises(ValueError) as excinfo:
        task_func("")
    assert "text cannot be empty." in str(excinfo.value)

    # Test case 2: text contains only letters
    text = "abcdefghijklmnopqrstuvwxyz"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(c.islower() for c in password)
    assert any(c.isdigit() for c in password)

    # Test case 3: text contains only digits
    text = "0123456789"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(c.isdigit() for c in password)
    assert any(c.islower() for c in password)

    # Test case 4: text contains letters, digits, and spaces
    text = "abcdefghijklmnopqrstuvwxyz0123456789 "
    password = task_func(text)
    assert len(password) == len(text)
    assert any(c.islower() for c in password)
    assert any(c.isdigit() for c in password)
    assert " " in password