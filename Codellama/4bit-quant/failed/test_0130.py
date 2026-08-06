import pytest
from src_0130 import task_func

def test_task_func():
    # Test with a valid URL
    url = 'http://example.com'
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert len(df.columns) > 0
    assert len(df.index) > 0

    # Test with a URL that raises a ConnectionError
    url = 'http://example.com/invalid'
    with pytest.raises(ConnectionError):
        task_func(url)

    # Test with a URL that raises a ValueError
    url = 'http://example.com/invalid'
    with pytest.raises(ValueError):
        task_func(url)