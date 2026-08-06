import pytest
from src_0929 import task_func

def test_task_func_with_empty_string():
    result = task_func('')
    assert result == {}

def test_task_func_with_single_character():
    result = task_func('a')
    assert result == {}

def test_task_func_with_two_characters():
    result = task_func('ab')
    assert result == {'ab': 1, 'ba': 0, 'aa': 0, 'bb': 0}

def test_task_func_with_repeated_characters():
    result = task_func('aaa')
    assert result == {'aa': 2, 'ab': 0, 'ba': 0, 'bb': 0}

def test_task_func_with_all_alphabets():
    result = task_func(string.ascii_lowercase)
    expected = {x*2: 1 for x in string.ascii_lowercase}
    for perm in itertools.permutations(string.ascii_lowercase, 2):
        expected[''.join(perm)] = 1
    assert result == expected

def test_task_func_with_non_alphabetic_characters():
    result = task_func('a!b')
    assert result == {'ab': 1, 'ba': 0, 'aa': 0, 'bb': 0}

def test_task_func_with_mixed_case():
    result = task_func('Abc')
    assert result == {'Ab': 1, 'bA': 0, 'bc': 1, 'cb': 0, 'cc': 0}

def test_task_func_with_large_input():
    result = task_func(''.join(itertools.repeat('a', 100)))
    assert result == {'aa': 99, 'ab': 0, 'ba': 0, 'bb': 0}