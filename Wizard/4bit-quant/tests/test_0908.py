python
import os
import re
import pytest

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    try:
        for file in os.listdir(directory):
            if re.search(pattern, file):
                new_filename = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        return False

def test_task_func():
    # Test case 1: Valid input
    assert task_func('abc', 'def', '.') == True
    
    # Test case 2: Invalid input (pattern not found)
    assert task_func('xyz', 'def', '.') == False
    
    # Test case 3: Invalid input (directory does not exist)
    assert task_func('abc', 'def', 'nonexistent_directory') == False
    
    # Test case 4: Invalid input (pattern is empty)
    assert task_func('', 'def', '.') == False
    
    # Test case 5: Invalid input (replacement is empty)
    assert task_func('abc', '', '.') == False
    
    # Test case 6: Invalid input (pattern is None)
    assert task_func(None, 'def', '.') == False
    
    # Test case 7: Invalid input (replacement is None)
    assert task_func('abc', None, '.') == False
    
    # Test case 8: Invalid input (directory is None)
    assert task_func('abc', 'def', None) == False