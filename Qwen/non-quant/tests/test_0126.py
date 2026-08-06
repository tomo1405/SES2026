import pytest
from src_0126 import task_func
from collections import defaultdict
import itertools
import json
import os

def test_task_func():
    # Test with simple input
    LETTERS = ['A', 'B', 'C']
    n = 2
    filename = task_func(LETTERS, n)
    
    # Check if file exists
    assert os.path.exists(filename)
    
    # Read the JSON file
    with open(filename, 'r') as f:
        letter_counts = json.load(f)
    
    # Expected letter counts
    expected_counts = defaultdict(int)
    for combination in itertools.combinations(LETTERS, n):
        for letter in combination:
            expected_counts[letter] += 1
    
    # Compare the actual and expected letter counts
    assert letter_counts == dict(expected_counts)
    
    # Clean up the created file
    os.remove(filename)

def test_task_func_with_single_letter():
    # Test with a single letter
    LETTERS = ['X']
    n = 1
    filename = task_func(LETTERS, n)
    
    # Check if file exists
    assert os.path.exists(filename)
    
    # Read the JSON file
    with open(filename, 'r') as f:
        letter_counts = json.load(f)
    
    # Expected letter counts
    expected_counts = {'X': 1}
    
    # Compare the actual and expected letter counts
    assert letter_counts == expected_counts
    
    # Clean up the created file
    os.remove(filename)

def test_task_func_with_no_combinations():
    # Test with no combinations possible
    LETTERS = ['A', 'B', 'C']
    n = 4
    filename = task_func(LETTERS, n)
    
    # Check if file exists
    assert os.path.exists(filename)
    
    # Read the JSON file
    with open(filename, 'r') as f:
        letter_counts = json.load(f)
    
    # Expected letter counts
    expected_counts = {}
    
    # Compare the actual and expected letter counts
    assert letter_counts == expected_counts
    
    # Clean up the created file
    os.remove(filename)