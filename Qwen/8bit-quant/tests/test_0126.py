import pytest
from src_0126 import task_func
from collections import defaultdict
import itertools
import json
import os

def test_task_func():
    LETTERS = ['A', 'B', 'C']
    n = 2
    filename = task_func(LETTERS, n)
    
    # Check if the file exists
    assert os.path.exists(filename), f"File {filename} does not exist"
    
    # Read the JSON file
    with open(filename, 'r') as f:
        letter_counts = json.load(f)
    
    # Calculate expected letter counts
    expected_letter_counts = defaultdict(int)
    combinations = list(itertools.combinations(LETTERS, n))
    for combination in combinations:
        for letter in combination:
            expected_letter_counts[letter] += 1
    
    # Compare the expected and actual letter counts
    assert letter_counts == dict(expected_letter_counts), f"Expected {expected_letter_counts}, but got {letter_counts}"
    
    # Clean up the created file
    os.remove(filename)