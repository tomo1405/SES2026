python
import random
import string
import pytest
from src_0339 import task_func

def test_task_func():
    elements = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    random_patterns, ax, char_count = task_func(elements)

    # Check if the number of patterns is correct
    assert len(random_patterns) == len(elements)

    # Check if the patterns are valid
    for pattern in random_patterns:
        assert '%' in pattern
        assert '%' in pattern.replace('%', '')
        assert len(pattern.replace('%', '')) == 5

    # Check if the histogram plot is correct
    assert ax.get_title() == 'Character occurrences'
    assert ax.get_xlabel() == 'Character'
    assert ax.get_ylabel() == 'Count'

    # Check if the character count is correct
    assert len(char_count) == 52
    assert char_count['a'] == 1
    assert char_count['b'] == 1
    assert char_count['c'] == 1
    assert char_count['d'] == 1
    assert char_count['e'] == 1
    assert char_count['f'] == 1
    assert char_count['g'] == 1
    assert char_count['h'] == 1
    assert char_count['i'] == 1
    assert char_count['j'] == 1
    assert char_count['k'] == 1
    assert char_count['l'] == 1
    assert char_count['m'] == 1
    assert char_count['n'] == 1
    assert char_count['o'] == 1
    assert char_count['p'] == 1
    assert char_count['q'] == 1
    assert char_count['r'] == 1
    assert char_count['s'] == 1
    assert char_count['t'] == 1
    assert char_count['u'] == 1
    assert char_count['v'] == 1
    assert char_count['w'] == 1
    assert char_count['x'] == 1
    assert char_count['y'] == 1
    assert char_count['z'] == 1
    assert char_count['0'] == 1
    assert char_count['1'] == 1
    assert char_count['2'] == 1
    assert char_count['3'] == 1
    assert char_count['4'] == 1
    assert char_count['5'] == 1
    assert char_count['6'] == 1
    assert char_count['7'] == 1
    assert char_count['8'] == 1
    assert char_count['9'] == 1