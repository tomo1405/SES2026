import pytest
from src_0178 import task_func

def test_task_func_with_valid_dataframe():
    df = pd.DataFrame({'Title': ['This is a title', 'This is another title'],
                       'Content': ['This is some content', 'This is more content']})
    word_freq = task_func(df)
    assert isinstance(word_freq, dict)
    assert len(word_freq) == 4
    assert 'this' in word_freq
    assert 'is' in word_freq
    assert 'a' in word_freq
    assert 'title' in word_freq
    assert 'content' in word_freq
    assert 'more' in word_freq

def test_task_func_with_invalid_dataframe():
    df = pd.DataFrame({'Title': ['This is a title', 'This is another title'],
                       'Content': ['This is some content', 'This is more content']})
    with pytest.raises(ValueError):
        task_func(df)