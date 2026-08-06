import string

import matplotlib.pyplot as plt
import pytest
from src_0437 import task_func


def test_task_func_type_error():
    with pytest.raises(TypeError, match="Expected string input"):
        task_func(123)

def test_task_func_empty_string():
    result, ax = task_func("")
    assert result == {letter: 0 for letter in string.ascii_lowercase}
    plt.close(ax.figure)

def test_task_func_single_letter():
    result, ax = task_func("a")
    expected = {letter: 0 for letter in string.ascii_lowercase}
    expected['a'] = 1
    assert result == expected
    plt.close(ax.figure)

def test_task_func_multiple_letters():
    result, ax = task_func("abc abc")
    expected = {letter: 0 for letter in string.ascii_lowercase}
    expected['a'] = 2
    expected['b'] = 2
    expected['c'] = 2
    assert result == expected
    plt.close(ax.figure)

def test_task_func_case_insensitivity():
    result, ax = task_func("AbC")
    expected = {letter: 0 for letter in string.ascii_lowercase}
    expected['a'] = 1
    expected['b'] = 1
    expected['c'] = 1
    assert result == expected
    plt.close(ax.figure)