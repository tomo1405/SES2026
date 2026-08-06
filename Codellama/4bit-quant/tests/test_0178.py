import pandas as pd
import pytest
from src_0178 import task_func


def test_task_func():
    # Test case 1: DataFrame with required columns
    df = pd.DataFrame({'Title': ['like', 'what'], 'Content': ['like', 'what']})
    word_freq = task_func(df)
    assert word_freq == {'like': 2, 'what': 2}

    # Test case 2: DataFrame without required columns
    df = pd.DataFrame({'Title': ['like', 'what'], 'Content': ['like', 'what']})
    with pytest.raises(ValueError):
        task_func(df)

    # Test case 3: DataFrame with empty 'Content' column
    df = pd.DataFrame({'Title': ['like', 'what'], 'Content': ['', '']})
    word_freq = task_func(df)
    assert word_freq == {}

    # Test case 4: DataFrame with non-empty 'Content' column
    df = pd.DataFrame({'Title': ['like', 'what'], 'Content': ['like', 'what']})
    word_freq = task_func(df)
    assert word_freq == {'like': 2, 'what': 2}