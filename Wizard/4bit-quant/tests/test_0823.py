python
import random
import string
import pytest

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
    # Test case 1: length is a positive integer
    assert task_func(10, 2) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'

    # Test case 2: num_digits is a non-negative integer and less than or equal to length
    assert task_func(10, 0) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'
    assert task_func(10, 1) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'
    assert task_func(10, 5) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'
    assert task_func(10, 10) == 'b9c8d7e6f5g4h3i2j1k0l7m6n5o4p3q2r1s0t'

    # Test case 3: length is not a positive integer
    with pytest.raises(ValueError):
        task_func(0, 2)

    # Test case 4: num_digits is not a non-negative integer and less than or equal to length
    with pytest.raises(ValueError):
        task_func(10, -1)
    with pytest.raises(ValueError):
        task_func(10, 11)