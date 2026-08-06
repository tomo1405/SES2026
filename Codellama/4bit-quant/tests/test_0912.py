import pytest
from src_0912 import task_func

def test_task_func():
    # Test case 1: Empty input
    assert task_func([]) == 1
    
    # Test case 2: Single letter input
    assert task_func(['A']) == 1
    
    # Test case 3: Multiple letter input
    assert task_func(['A', 'B', 'C']) == 6
    
    # Test case 4: Input with duplicate letters
    assert task_func(['A', 'B', 'C', 'A']) == 6
    
    # Test case 5: Input with letters out of order
    assert task_func(['C', 'B', 'A']) == 6
    
    # Test case 6: Input with letters out of order and duplicate letters
    assert task_func(['C', 'B', 'A', 'A']) == 6