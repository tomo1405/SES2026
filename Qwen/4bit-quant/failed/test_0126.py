import pytest
from src_0126 import task_func
import os
import json
from collections import defaultdict

def test_task_func():
    LETTERS = ['a', 'b', 'c']
    n = 2

    # Capture the output filename
    filename = task_func(LETTERS, n)

    # Check if the file exists
    assert os.path.exists(filename), f"File {filename} does not exist"

    # Read the content of the file
    with open(filename, 'r') as f:
        content = json.load(f)

    # Expected combinations and their counts
    expected_combinations = list(itertools.combinations(LETTERS, n))
    expected_letter_counts = defaultdict(int)
    for combination in expected_combinations:
        for letter in combination:
            expected_letter_counts[letter] += 1

    # Check if the content matches the expected letter counts
    assert content == expected_letter_counts, f"Content {content} does not match expected letter counts {expected_letter_counts}"

    # Clean up: remove the created file
    os.remove(filename)