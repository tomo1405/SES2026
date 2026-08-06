python
import numpy as np
import random
from difflib import SequenceMatcher

def task_func(s, min_length, max_length, letters):
    string_length = np.random.randint(min_length, max_length+1)
    generated_s = ''.join(random.choice(letters) for _ in range(string_length))

    # Check similarity
    similarity = SequenceMatcher(None, s, generated_s).ratio()
    is_similar = similarity >= 0.5

    return generated_s, is_similar

def test_task_func():
    # Test case 1
    s = "hello"
    min_length = 5
    max_length = 10
    letters = "abcde"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    assert len(generated_s) >= min_length and len(generated_s) <= max_length
    assert all(c in letters for c in generated_s)
    assert is_similar == True

    # Test case 2
    s = "world"
    min_length = 5
    max_length = 10
    letters = "abcde"
    generated_s, is_similar = task_func(s, min_length, max_length, letters)
    assert len(generated_s) >= min_length and len(generated_s) <= max_length
    assert all(c in letters for c in generated_s)
    assert is_similar == False