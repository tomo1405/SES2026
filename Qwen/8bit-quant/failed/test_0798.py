import pytest
from src_0798 import task_func
import pandas as pd

def test_task_func_with_empty_dataframe():
    df = pd.DataFrame()
    assert task_func(df) == 0

def test_task_func_with_no_brackets():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['a', 'b', 'c']
    })
    assert task_func(df) == 0

def test_task_func_with_brackets():
    df = pd.DataFrame({
        'A': ['(a)', '[b]', '{c}'],
        'B': ['{d}', '(e)', '[f]']
    })
    assert task_func(df) == 6

def test_task_func_with_mixed_data():
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': ['(a)', '[b]', '{c}'],
        'C': ['no brackets', '()', '{}[]']
    })
    assert task_func(df) == 6

def test_task_func_with_non_dataframe_input():
    with pytest.raises(TypeError):
        task_func([1, 2, 3])

def test_task_func_with_single_character_brackets():
    df = pd.DataFrame({
        'A': ['(', ')', '[', ']', '{', '}']
    })
    assert task_func(df) == 6

def test_task_func_with_nested_brackets():
    df = pd.DataFrame({
        'A': ['((a))', '[{b}]', '{{c}}']
    })
    assert task_func(df) == 6