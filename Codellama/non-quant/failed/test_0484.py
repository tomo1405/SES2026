import pytest
from src_0484 import task_func
import pandas as pd

def test_task_func_with_valid_input():
    df = pd.DataFrame({'text': ['hello world', 'hello python', 'hello world']})
    pattern = 'hello'
    expected_output = pd.DataFrame({'text': ['world hello', 'python hello', 'world hello']})
    output = task_func(df, 'text', pattern)
    assert output.equals(expected_output)

def test_task_func_with_invalid_input():
    df = pd.DataFrame({'text': ['hello world', 'hello python', 'hello world']})
    pattern = 'goodbye'
    expected_output = pd.DataFrame({'text': ['hello world', 'hello python', 'hello world']})
    output = task_func(df, 'text', pattern)
    assert output.equals(expected_output)

def test_task_func_with_empty_pattern():
    df = pd.DataFrame({'text': ['hello world', 'hello python', 'hello world']})
    pattern = ''
    expected_output = pd.DataFrame({'text': ['hello world', 'hello python', 'hello world']})
    output = task_func(df, 'text', pattern)
    assert output.equals(expected_output)