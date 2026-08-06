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
    # Test case 1: text with only letters
    text = "Hello World"
    expected_password = "hEllO wOrld"
    assert task_func(text) == expected_password

    # Test case 2: text with only digits
    text = "1234567890"
    expected_password = "1234567890"
    assert task_func(text) == expected_password

    # Test case 3: text with mixed characters
    text = "Hello 123 World"
    expected_password = "hEllO 123 wOrld"
    assert task_func(text) == expected_password

    # Test case 4: text with mixed characters and spaces
    text = "Hello 123 World"
    expected_password = "hEllO 123 wOrld"
    assert task_func(text) == expected_password

    # Test case 5: text with empty string
    text = ""
    with pytest.raises(ValueError):
        task_func(text)

    # Test case 6: text with None
    text = None
    with pytest.raises(TypeError):
        task_func(text)

    # Test case 7: text with seed
    text = "Hello World"
    seed = 12345
    expected_password = "hEllO wOrld"
    assert task_func(text, seed) == expected_password