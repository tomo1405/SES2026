python
import random
import string
import pytest

# Constants
LETTERS = string.ascii_letters

def task_func(num_words, word_length):
    # Validate input parameters
    if num_words < 0 or word_length < 0:
        raise ValueError("num_words and word_length must be non-negative")

    random.seed(42)
    words = [''.join(random.choice(LETTERS) for _ in range(word_length)) for _ in range(num_words)]
    
    return words

def test_task_func():
    # Test case 1: num_words = 3, word_length = 5
    assert task_func(3, 5) == ['yJG', 'vKZ', 'fLh']

    # Test case 2: num_words = 0, word_length = 5
    with pytest.raises(ValueError):
        task_func(0, 5)

    # Test case 3: num_words = 3, word_length = -5
    with pytest.raises(ValueError):
        task_func(3, -5)