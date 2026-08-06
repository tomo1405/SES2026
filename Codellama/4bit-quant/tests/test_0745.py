import pandas as pd
import pytest
from src_0745 import task_func


def test_task_func():
    # Test 1: Input is a string
    text = "This is a test string"
    df = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 2
    assert df.columns.tolist() == ["Word", "Frequency"]

    # Test 2: Input is not a string
    text = 123
    with pytest.raises(ValueError):
        task_func(text)

    # Test 3: Input is an empty string
    text = ""
    df = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 0
    assert df.columns.tolist() == ["Word", "Frequency"]

    # Test 4: Input contains multiple dollar signs
    text = "This is a test string with $100 and $200"
    df = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 2
    assert df.columns.tolist() == ["Word", "Frequency"]
    assert df.iloc[0, 0] == "$100"
    assert df.iloc[0, 1] == 1
    assert df.iloc[1, 0] == "$200"
    assert df.iloc[1, 1] == 1

    # Test 5: Input contains punctuation
    text = "This is a test string with $100 and $200."
    df = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 2
    assert df.columns.tolist() == ["Word", "Frequency"]
    assert df.iloc[0, 0] == "$100"
    assert df.iloc[0, 1] == 1
    assert df.iloc[1, 0] == "$200"
    assert df.iloc[1, 1] == 1

    # Test 6: Input contains multiple dollar signs and punctuation
    text = "This is a test string with $100 and $200. The price is $300."
    df = task_func(text)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] == 3
    assert df.columns.tolist() == ["Word", "Frequency"]
    assert df.iloc[0, 0] == "$100"
    assert df.iloc[0, 1] == 1
    assert df.iloc[1, 0] == "$200"
    assert df.iloc[1, 1] == 1
    assert df.iloc[2, 0] == "$300"
    assert df.iloc[2, 1] == 1