import pandas as pd
from src_0484 import task_func


def test_task_func():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = 'world'
    expected_output = pd.DataFrame({'A': ['world hello', 'world goodbye']})
    assert task_func(df, 'A', pattern).equals(expected_output)

def test_task_func_no_pattern():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = ''
    expected_output = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    assert task_func(df, 'A', pattern).equals(expected_output)

def test_task_func_no_column():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = 'world'
    expected_output = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    assert task_func(df, 'B', pattern).equals(expected_output)

def test_task_func_no_dataframe():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = 'world'
    expected_output = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    assert task_func(None, 'A', pattern).equals(expected_output)

def test_task_func_no_pattern_no_column():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = ''
    expected_output = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    assert task_func(df, None, pattern).equals(expected_output)

def test_task_func_no_pattern_no_dataframe():
    df = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    pattern = ''
    expected_output = pd.DataFrame({'A': ['hello world', 'goodbye world']})
    assert task_func(None, None, pattern).equals(expected_output)