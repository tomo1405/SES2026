import urllib
from datetime import datetime

import pandas as pd
import pytest
from src_0591 import task_func


def test_task_func():
    url = "https://www.example.com"
    df = task_func(url)
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['text', 'href', 'fetch_time']
    assert df['fetch_time'].iloc[0] == datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def test_task_func_with_invalid_url():
    with pytest.raises(ValueError) as exc_info:
        task_func("")
    assert "URL must not be empty." in str(exc_info.value)

def test_task_func_with_invalid_url_2():
    with pytest.raises(urllib.error.URLError) as exc_info:
        task_func("invalid_url")
    assert "Error fetching URL invalid_url" in str(exc_info.value)