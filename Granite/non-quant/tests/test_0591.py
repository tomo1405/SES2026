import urllib

import pytest
from src_0591 import task_func


def test_task_func():
    with pytest.raises(ValueError):
        task_func("")

    with pytest.raises(urllib.error.URLError):
        task_func("invalid_url")

    df = task_func("valid_url")
    assert isinstance(df, pd.DataFrame)
    assert df.columns.tolist() == ['text', 'href', 'fetch_time']