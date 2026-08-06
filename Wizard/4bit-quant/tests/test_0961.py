python
import string
import random
import pytest

def task_func(text, seed=None):
    if seed is not None:
        random.seed(seed)
    if not text:
        raise ValueError("text cannot be empty.")
    password = ""
    for char in text:
        random_lowercase = random.choice(string.ascii_lowercase)
        random_digit = random.choice(string.digits)
        if char.isalpha():
            password += random_lowercase
        elif char.isdigit():
            password += random_digit
        elif char == " ":
            if random.random() < 0.5:
                password += random_lowercase
            else:
                password += random_digit
        else:
            password += char
    return password

def test_task_func():
    # Test case 1: text is empty
    with pytest.raises(ValueError):
        task_func("")

    # Test case 2: text contains only alphabets
    text = "abc"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isalpha() for char in password)

    # Test case 3: text contains only digits
    text = "123"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isdigit() for char in password)

    # Test case 4: text contains alphabets and digits
    text = "abc123"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isalpha() or char.isdigit() for char in password)

    # Test case 5: text contains special characters
    text = "abc!@#123"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isalpha() or char.isdigit() or char in "!@#" for char in password)

    # Test case 6: text contains spaces
    text = "abc 123"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isalpha() or char.isdigit() or char in "!@#" for char in password)
    assert password.count(string.ascii_lowercase) == password.count(string.digits)

    # Test case 7: text contains spaces and special characters
    text = "abc!@# 123"
    password = task_func(text)
    assert len(password) == len(text)
    assert all(char.isalpha() or char.isdigit() or char in "!@#" for char in password)
    assert password.count(string.ascii_lowercase) == password.count(string.digits)

    # Test case 8: text contains spaces and special characters with seed
    text = "abc!@# 123"
    password = task_func(text, seed=123)
    assert len(password) == len(text)
    assert all(char.isalpha() or char.isdigit() or char in "!@#" for char in password)
    assert password.count(string.ascii_lowercase) == password.count(string.digits)
    assert password == "a!@# 123"