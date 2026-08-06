import re
import pandas as pd
from src_0484 import task_func

def test_task_func():
    df = pd.DataFrame({'column': ['hello world', 'goodbye world', 'hello there']})
    new_df = task_func(df, 'column', 'hello')
    assert new_df['column'][0] == 'world hello'
    assert new_df['column'][1] == 'goodbye world'
    assert new_df['column'][2] == 'hello there'

def test_task_func_no_pattern():
    df = pd.DataFrame({'column': ['hello world', 'goodbye world', 'hello there']})
    new_df = task_func(df, 'column', '')
    assert new_df['column'][0] == 'hello world'
    assert new_df['column'][1] == 'goodbye world'
    assert new_df['column'][2] == 'hello there'

def test_task_func_no_column():
    df = pd.DataFrame({'column': ['hello world', 'goodbye world', 'hello there']})
    new_df = task_func(df, '', 'hello')
    assert new_df['column'][0] == 'hello world'
    assert new_df['column'][1] == 'goodbye world'
    assert new_df['column'][2] == 'hello there'

def test_task_func_no_column_no_pattern():
    df = pd.DataFrame({'column': ['hello world', 'goodbye world', 'hello there']})
    new_df = task_func(df, '', '')
    assert new_df['column'][0] == 'hello world'
    assert new_df['column'][1] == 'goodbye world'
    assert new_df['column'][2] == 'hello there'