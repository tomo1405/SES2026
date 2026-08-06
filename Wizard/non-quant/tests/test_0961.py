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

    # Test case 2: text contains only spaces
    assert task_func("   ") == "   "

    # Test case 3: text contains only digits
    assert task_func("1234567890") == "1234567890"

    # Test case 4: text contains only lowercase letters
    assert task_func("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz"

    # Test case 5: text contains only uppercase letters
    assert task_func("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Test case 6: text contains mixed case letters and digits
    assert task_func("Abc123def456ghi789jkl012mno345pqr678stu901vwxyz") == "Abc123def456ghi789jkl012mno345pqr678stu901vwxyz"

    # Test case 7: text contains mixed case letters, digits, and spaces
    assert task_func("Abc 123 def 456 ghi 789 jkl 012 mno 345 pqr 678 stu 901 vwxyz") == "Abc 123 def 456 ghi 789 jkl 012 mno 345 pqr 678 stu 901 vwxyz"

    # Test case 8: text contains mixed case letters, digits, spaces, and special characters
    assert task_func("Abc 123 def 456 ghi 789 jkl 012 mno 345 pqr 678 stu 901 vwxyz!@#$%^&*()_+-=[]{}|;':\",./<>?") == "Abc 123 def 456 ghi 789 jkl 012 mno 345 pqr 678 stu 901 vwxyz!@#$%^&*()_+-=[]{}|;':\",./<>?"

    # Test case 9: text contains only special characters
    assert task_func("!@#$%^&*()_+-=[]{}|;':\",./<>?") == "!@#$%^&*()_+-=[]{}|;':\",./<>?"

    # Test case 10: text contains only special characters and spaces
    assert task_func("!@#$%^&*()_+-=[]{}|;':\",./<>?   ") == "!@#$%^&*()_+-=[]{}|;':\",./<>?   "

    # Test case 11: text contains only special characters and spaces, with seed
    assert task_func("!@#$%^&*()_+-=[]{}|;':\",./<>?   ", seed=42) == "1!@#$%^&*()_+-=[]{}|;':\",./<>?   "

    # Test case 12: text contains only special characters and spaces, with different seed
    assert task_func("!@#$%^&*()_+-=[]{}|;':\",./<>?   ", seed=123) == "1!@#$%^&*()_+-=[]{}|;':\",./<>?   "