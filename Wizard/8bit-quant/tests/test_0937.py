python
import numpy as np
import matplotlib.pyplot as plt
import string
# Constants
ALPHABET = list(string.ascii_lowercase)

def test_task_func():
    # Test case 1: Valid input word
    word = 'python'
    expected_result = np.array([1, 2, 3, 4, 5])
    result = task_func(word)
    assert np.array_equal(result.get_xticks(), expected_result)
    
    # Test case 2: Invalid input word (contains non-alphabetic characters)
    word = 'Python3'
    try:
        task_func(word)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
        
    # Test case 3: Invalid input word (contains uppercase characters)
    word = 'PYTHON'
    try:
        task_func(word)
        assert False, "Expected ValueError"
    except ValueError:
        assert True