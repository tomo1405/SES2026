import pytest
from src_0937 import task_func

def test_task_func_valid_input():
    # Test with a valid input
    word = 'hello'
    ax = task_func(word)
    assert ax.get_xlabel() == 'Letter Index'
    assert ax.get_ylabel() == 'Alphabetical Position'
    assert ax.get_title() == 'Alphabetical Position of Letters in Word'
    assert len(ax.get_xticks()) == len(word)
    assert len(ax.get_yticks()) == len(ALPHABET)
    assert all(char in ALPHABET for char in word)

def test_task_func_invalid_input():
    # Test with an invalid input
    word = 'hello1'
    with pytest.raises(ValueError):
        task_func(word)