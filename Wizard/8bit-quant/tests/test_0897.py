python
import pytest
from src_0897 import task_func

def test_task_func():
    # Test case 1
    assert task_func(5, 10, 0) == {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
    
    # Test case 2
    assert task_func(3, 5, 1) == {'a': 10, 'b': 10, 'c': 10, 'd': 10, 'e': 10}
    
    # Test case 3
    assert task_func(2, 10, 2) == {'aa': 5, 'ab': 5, 'ac': 5, 'ad': 5, 'ae': 5, 'ba': 5, 'bb': 5, 'bc': 5, 'bd': 5, 'be': 5, 'ca': 5, 'cb': 5, 'cc': 5, 'cd': 5, 'ce': 5, 'da': 5, 'db': 5, 'dc': 5, 'dd': 5, 'de': 5, 'ea': 5, 'eb': 5, 'ec': 5, 'ed': 5, 'ee': 5}