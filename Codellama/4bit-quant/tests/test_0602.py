import pandas as pd
import pytest
from src_0602 import task_func


def test_task_func():
    # Test if the function raises an error when the DataFrame does not contain a 'Word' column
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    with pytest.raises(ValueError):
        task_func(df, 'a')

    # Test if the function returns None when the DataFrame is empty
    df = pd.DataFrame()
    assert task_func(df, 'a') is None

    # Test if the function returns a valid boxplot when the DataFrame is not empty
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    ax = task_func(df, 'a')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'a'"

    # Test if the function returns a valid boxplot when the DataFrame contains multiple words starting with the same letter
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'durian']})
    ax = task_func(df, 'a')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'a'"

    # Test if the function returns a valid boxplot when the DataFrame contains multiple words starting with different letters
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry', 'durian', 'elderberry']})
    ax = task_func(df, 'a')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'a'"
    ax = task_func(df, 'b')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'b'"
    ax = task_func(df, 'c')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'c'"
    ax = task_func(df, 'd')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'd'"
    ax = task_func(df, 'e')
    assert isinstance(ax, sns.boxplot)
    assert ax.get_title() == "Word Lengths Distribution for Words Starting with 'e'"