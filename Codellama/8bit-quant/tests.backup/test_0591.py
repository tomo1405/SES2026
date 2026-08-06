import pytest
from src_0591 import task_func

def test_task_func_valid_url():
    url = "https://www.example.com"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.shape[0] > 0
    assert "text" in df.columns
    assert "href" in df.columns
    assert "fetch_time" in df.columns

def test_task_func_invalid_url():
    url = ""
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_url_error():
    url = "https://www.example.com/invalid"
    with pytest.raises(urllib.error.URLError):
        task_func(url)