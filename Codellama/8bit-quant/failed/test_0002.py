import pytest
from src_0002 import task_func

def test_task_func_length_less_than_zero():
    with pytest.raises(ValueError):
        task_func(length=-1)

def test_task_func_length_zero():
    assert task_func(length=0) == {}

def test_task_func_length_one():
    assert task_func(length=1) == {'a': 1}

def test_task_func_length_two():
    assert task_func(length=2) == {'a': 1, 'b': 1}

def test_task_func_length_three():
    assert task_func(length=3) == {'a': 1, 'b': 1, 'c': 1}

def test_task_func_length_four():
    assert task_func(length=4) == {'a': 1, 'b': 1, 'c': 1, 'd': 1}

def test_task_func_length_five():
    assert task_func(length=5) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}

def test_task_func_length_six():
    assert task_func(length=6) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1}

def test_task_func_length_seven():
    assert task_func(length=7) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1}

def test_task_func_length_eight():
    assert task_func(length=8) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1}

def test_task_func_length_nine():
    assert task_func(length=9) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1}

def test_task_func_length_ten():
    assert task_func(length=10) == {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1}