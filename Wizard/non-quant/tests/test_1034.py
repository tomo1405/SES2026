python
import itertools
import string
import pandas as pd
import pytest

def task_func():
    LETTERS = list(string.ascii_lowercase)
    combinations = list(itertools.product(LETTERS, repeat=3))
    df = pd.DataFrame(combinations, columns=["a", "b", "c"])

    # Getting value counts and ensuring the correct order of letters
    value_counts = df["a"].value_counts().reindex(LETTERS, fill_value=0)

    # Plotting the histogram with the correct order
    ax = value_counts.plot(kind="bar")

    return df, ax

def test_task_func():
    df, ax = task_func()
    assert df.shape == (26 ** 3, 3)
    assert ax.get_xlabel() == "a"
    assert ax.get_ylabel() == "Frequency"