import pandas as pd
from src_0602 import task_func


def test_task_func_valid_input():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is not None
    assert ax.get_title() == f"Word Lengths Distribution for Words Starting with '{letter}'"
    assert ax.get_xlabel() == 'Word Length'
    assert ax.get_ylabel() == 'Count'
    assert len(ax.get_xticks()) == 3
    assert len(ax.get_yticks()) == 3

def test_task_func_invalid_input():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'z'
    ax = task_func(df, letter)
    assert ax is None
    assert ax.get_title() == f"No words start with the letter '{letter}'."
    assert ax.get_xlabel() == 'Word Length'
    assert ax.get_ylabel() == 'Count'
    assert len(ax.get_xticks()) == 0
    assert len(ax.get_yticks()) == 0

def test_task_func_empty_input():
    df = pd.DataFrame()
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is None
    assert ax.get_title() == "The DataFrame is empty."
    assert ax.get_xlabel() == 'Word Length'
    assert ax.get_ylabel() == 'Count'
    assert len(ax.get_xticks()) == 0
    assert len(ax.get_yticks()) == 0