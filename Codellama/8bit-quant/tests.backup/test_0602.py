import pytest
from src_0602 import task_func

def test_task_func_valid_input():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is not None
    assert ax.get_title() == f"Word Lengths Distribution for Words Starting with '{letter}'"
    assert ax.get_xlabel() == 'Word Length'
    assert ax.get_ylabel() == 'Count'

def test_task_func_invalid_input():
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'z'
    ax = task_func(df, letter)
    assert ax is None
    assert ax.get_title() == f"No words start with the letter '{letter}'."

def test_task_func_empty_input():
    df = pd.DataFrame()
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is None
    assert ax.get_title() == "The DataFrame is empty."

def test_task_func_no_word_column():
    df = pd.DataFrame({'Fruit': ['apple', 'banana', 'cherry']})
    letter = 'a'
    with pytest.raises(ValueError):
        task_func(df, letter)