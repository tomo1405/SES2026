python
import pytest
from src_0937 import task_func

def test_task_func():
    # Test case 1: Valid input word
    word = 'python'
    ax = task_func(word)
    assert isinstance(ax, plt.Axes)
    
    # Test case 2: Invalid input word (contains non-alphabetic characters)
    word = 'Python3'
    with pytest.raises(ValueError):
        task_func(word)