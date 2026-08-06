import pytest
from src_0776 import task_func
from string import ascii_lowercase
import re
from collections import Counter

# Constants
LETTERS_PATTERN = re.compile(r'^(.*?)-[a-z]$')
LETTERS = ascii_lowercase

def test_task_func():
    assert task_func("abc-def") == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}
    assert task_func("abc-xyz") == {'a': 1, 'b': 1, 'c': 1}
    assert task_func("abc123") == {}
    assert task_func("") == {}