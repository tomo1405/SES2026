python
import random
import string
import pytest

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):

    random.seed(42)
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not (0 <= num_digits <= length):
        raise ValueError("num_digits must be a non-negative integer and less than or equal to length.")

    password = []
    for _ in range(length - num_digits):
        password.append(random.choice(LETTERS))
    for _ in range(num_digits):
        password.append(random.choice(DIGITS))

    random.shuffle(password)

    return ''.join(password)

def test_task_func():
    # Test case 1
    assert task_func(10, 2) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'

    # Test case 2
    assert task_func(10, 0) == 'abcdefghij'

    # Test case 3
    assert task_func(10, 10) == 'abcdefghij0123456789'

    # Test case 4
    with pytest.raises(ValueError):
        task_func(-10, 2)

    # Test case 5
    with pytest.raises(ValueError):
        task_func(10, -2)

    # Test case 6
    with pytest.raises(ValueError):
        task_func(10, 12)