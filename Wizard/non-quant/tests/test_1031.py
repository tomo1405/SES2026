python
import itertools
import string
import pandas as pd
import pytest

def task_func():
    LETTERS = list(string.ascii_lowercase)
    combinations = list(itertools.product(LETTERS, repeat=3))

    df = pd.DataFrame(combinations, columns=["Letter 1", "Letter 2", "Letter 3"])

    return df

def test_task_func():
    df = task_func()
    assert df.shape == (26 ** 3, 3)
    assert df.columns.tolist() == ["Letter 1", "Letter 2", "Letter 3"]
    assert df["Letter 1"].nunique() == 26
    assert df["Letter 2"].nunique() == 26
    assert df["Letter 3"].nunique() == 26