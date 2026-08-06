python
import pytest
from src_0720 import task_func

def test_task_func():
    # Test case 1: directory contains only one file, word is present
    directory = 'tests/test_data/task_func/case1'
    word = 'hello'
    expected_count = 1
    count = task_func(directory, word)
    assert count == expected_count
    
    # Test case 2: directory contains only one file, word is not present
    directory = 'tests/test_data/task_func/case2'
    word = 'world'
    expected_count = 0
    count = task_func(directory, word)
    assert count == expected_count
    
    # Test case 3: directory contains multiple files, word is present in all files
    directory = 'tests/test_data/task_func/case3'
    word = 'python'
    expected_count = 3
    count = task_func(directory, word)
    assert count == expected_count
    
    # Test case 4: directory contains multiple files, word is present in some files
    directory = 'tests/test_data/task_func/case4'
    word = 'hello'
    expected_count = 2
    count = task_func(directory, word)
    assert count == expected_count
    
    # Test case 5: directory contains multiple files, word is not present in any file
    directory = 'tests/test_data/task_func/case5'
    word = 'world'
    expected_count = 0
    count = task_func(directory, word)
    assert count == expected_count