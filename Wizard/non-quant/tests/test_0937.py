python
import numpy as np
import matplotlib.pyplot as plt
import string
# Constants
ALPHABET = list(string.ascii_lowercase)

def test_task_func():
    # Test case 1: Valid input word
    word = 'python'
    expected_result = plt.Axes
    assert isinstance(task_func(word), expected_result)
    
    # Test case 2: Invalid input word (contains non-alphabetic characters)
    word = 'Python3'
    expected_result = ValueError
    try:
        task_func(word)
    except ValueError as e:
        assert isinstance(e, expected_result)
        
    # Test case 3: Invalid input word (contains uppercase characters)
    word = 'PYTHON'
    expected_result = ValueError
    try:
        task_func(word)
    except ValueError as e:
        assert isinstance(e, expected_result)