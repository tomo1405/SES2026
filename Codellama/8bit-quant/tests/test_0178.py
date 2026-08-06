import pandas as pd
import pytest
from src_0178 import task_func


def test_task_func_with_valid_dataframe():
    df = pd.DataFrame({'Title': ['This is a title', 'This is another title'],
                      'Content': ['This is some content', 'This is more content']})
    word_freq = task_func(df)
    assert isinstance(word_freq, dict)
    assert len(word_freq) > 0

def test_task_func_with_invalid_dataframe():
    df = pd.DataFrame({'Title': ['This is a title', 'This is another title'],
                      'Content': ['This is some content', 'This is more content']})
    with pytest.raises(ValueError):
        task_func(df)