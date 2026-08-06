import pytest
from src_0126 import task_func

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    n = 2
    filename = task_func(LETTERS, n)
    assert filename == 'letter_combinations_1.json'

    with open(filename, 'r') as f:
        letter_counts = json.load(f)
        assert letter_counts == {'A': 1, 'B': 1, 'C': 1}