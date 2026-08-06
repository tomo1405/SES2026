import pytest
from src_1008 import task_func

def test_task_func_valid_url():
    url = "https://api.example.com/data"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_task_func_invalid_url():
    url = "https://api.example.com/data/invalid"
    with pytest.raises(ValueError):
        task_func(url)

def test_task_func_network_error():
    url = "https://api.example.com/data"
    with pytest.raises(SystemError):
        task_func(url)