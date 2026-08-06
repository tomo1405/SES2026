import pytest
from src_0484 import task_func
import pandas as pd

def test_task_func_no_pattern():
    df = pd.DataFrame({'text': ['hello world', 'hello python']})
    new_df = task_func(df, 'text', '')
    assert new_df.equals(df)

def test_task_func_with_pattern():
    df = pd.DataFrame({'text': ['hello world', 'hello python']})
    new_df = task_func(df, 'text', 'hello')
    assert new_df['text'][0] == 'world hello'
    assert new_df['text'][1] == 'python hello'