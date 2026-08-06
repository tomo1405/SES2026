import random
import string
from collections import defaultdict

from src_0863 import task_func


def test_task_func_with_seed():
    n = 10
    seed = 42
    result = task_func(n, seed)
    
    expected_output = defaultdict(list)
    random.seed(seed)
    LETTERS = string.ascii_lowercase
    for _ in range(n):
        letter = random.choice(LETTERS)
        expected_output[letter].append(letter)
    
    assert result == expected_output

def test_task_func_without_seed():
    n = 5
    result = task_func(n)
    assert len(result) <= n
    for letters in result.values():
        assert all(isinstance(letter, str) and len(letter) == 1 for letter in letters)

def test_task_func_zero_n():
    n = 0
    result = task_func(n)
    assert result == defaultdict(list)

def test_task_func_large_n():
    n = 1000
    seed = 123
    result = task_func(n, seed)
    
    expected_output = defaultdict(list)
    random.seed(seed)
    LETTERS = string.ascii_lowercase
    for _ in range(n):
        letter = random.choice(LETTERS)
        expected_output[letter].append(letter)
    
    assert result == expected_output