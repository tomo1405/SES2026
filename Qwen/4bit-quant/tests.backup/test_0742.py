import pytest
from src_0742 import task_func

def test_task_func_empty_dict():
    assert task_func({}) == {}

def test_task_func_single_key():
    assert task_func({'a': 1}) == {'a': 1}

def test_task_func_multiple_keys_same_prefix():
    assert task_func({'abc': 1, 'ab': 2, 'ac': 3}) == {'a': 6}

def test_task_func_multiple_keys_different_prefixes():
    assert task_func({'abc': 1, 'def': 2, 'ghi': 3}) == {'a': 1, 'd': 2, 'g': 3}

def test_task_func_mixed_case_keys():
    assert task_func({'Abc': 1, 'aB': 2, 'Ac': 3}) == {'A': 6}

def test_task_func_numeric_keys():
    assert task_func({123: 1, 124: 2, 125: 3}) == {'1': 6}

def test_task_func_mixed_key_types():
    with pytest.raises(TypeError):
        task_func({('a', 1): 1, ('b', 2): 2})

def test_task_func_negative_values():
    assert task_func({'abc': -1, 'ab': -2, 'ac': -3}) == {'a': -6}