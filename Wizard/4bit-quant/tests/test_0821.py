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
    # Test case 1: num_words = 0, word_length = 0
    assert task_func(0, 0) == []

    # Test case 2: num_words = 1, word_length = 1
    assert task_func(1, 1) == ['a']

    # Test case 3: num_words = 2, word_length = 2
    assert task_func(2, 2) == ['aA', 'bB']

    # Test case 4: num_words = 3, word_length = 3
    assert task_func(3, 3) == ['aA1', 'bB2', 'cC3']

    # Test case 5: num_words = 10, word_length = 5
    assert len(task_func(10, 5)) == 10
    assert all(len(word) == 5 for word in task_func(10, 5))
    assert all(word.isalpha() for word in task_func(10, 5))
    assert all(word.islower() for word in task_func(10, 5))
    assert all(word.isupper() for word in task_func(10, 5))

    # Test case 6: num_words = -1, word_length = 10
    with pytest.raises(ValueError):
        task_func(-1, 10)

    # Test case 7: num_words = 10, word_length = -1
    with pytest.raises(ValueError):
        task_func(10, -1)