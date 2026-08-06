import pytest
from collections import Counter
import itertools
import string

def task_func(word: str) -> dict:
    ALPHABETS = string.ascii_lowercase
    # Generate all two-letter combinations of alphabets
    permutations = [''.join(x) for x in itertools.permutations(ALPHABETS, 2)]
    combinations = permutations + [x*2 for x in ALPHABETS]
    
    # Generate all two-letter combinations in the word
    word_combinations = [''.join(x) for x in zip(word, word[1:])]
    # Count the occurrences of each two-letter combination in the word
    word_counter = Counter(word_combinations)

    # Create the dictionary with the counts
    return {key: word_counter.get(key, 0) for key in combinations}

def test_task_func():
    word = "abracadabra"
    expected_output = {'aa': 2, 'ab': 2, 'ac': 1, 'ad': 1, 'ae': 0, 'bb': 1, 'bc': 0, 'bd': 0, 'be': 0, 'cc': 1, 'cd': 0, 'ce': 0, 'dd': 0, 'de': 0, 'ee': 0, 'aaa': 0, 'aab': 0, 'aac': 0, 'aad': 0, 'aae': 0, 'bbb': 0, 'bbc': 0, 'bbd': 0, 'bbe': 0, 'ccc': 0, 'ccd': 0, 'cce': 0, 'ddd': 0, 'dde': 0, 'eee': 0}
    actual_output = task_func(word)
    assert actual_output == expected_output, "Output does not match the expected output"

test_task_func()