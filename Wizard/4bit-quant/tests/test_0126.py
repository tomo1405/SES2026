python
import itertools
import json
import random
from collections import defaultdict

def task_func(LETTERS, n):
    combinations = list(itertools.combinations(LETTERS, n))
    letter_counts = defaultdict(int)

    for combination in combinations:
        for letter in combination:
            letter_counts[letter] += 1

    filename = f'letter_combinations_{random.randint(1, 100)}.json'
    with open(filename, 'w') as f:
        json.dump(letter_counts, f)

    return filename

def test_task_func():
    LETTERS = 'abcde'
    n = 3
    filename = task_func(LETTERS, n)
    assert filename.startswith('letter_combinations_')
    assert filename.endswith('.json')
    with open(filename) as f:
        data = json.load(f)
        assert len(data) == len(LETTERS)
        for letter in LETTERS:
            assert letter in data
            assert data[letter] == 1