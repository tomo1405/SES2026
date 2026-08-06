import pytest
from src_0600 import task_func

def test_task_func():
    # Test with valid input
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is not None
    assert ax.get_title() == f"Histogram of Word Lengths starting with '{letter}'"
    assert ax.get_xlabel() == "Word Length"
    assert ax.get_ylabel() == "Frequency"

    # Test with invalid input
    df = pd.DataFrame({'Word': ['apple', 'banana', 'cherry']})
    letter = 'z'
    ax = task_func(df, letter)
    assert ax is None
    assert "No words start with the letter 'z'." in caplog.text

    # Test with empty input
    df = pd.DataFrame({'Word': []})
    letter = 'a'
    ax = task_func(df, letter)
    assert ax is None
    assert "No words start with the letter 'a'." in caplog.text