import urllib

import pandas as pd
import pytest
from src_0591 import task_func


def test_task_func_with_valid_url():
    url = "https://www.example.com"
    expected_df = pd.DataFrame(
        data=[
            ("Example Text", "https://www.example.com/example-link"),
            ("Another Text", "https://www.example.com/another-link")
        ],
        columns=['text', 'href', 'fetch_time']
    )
    actual_df = task_func(url)
    pd.testing.assert_frame_equal(expected_df, actual_df)

def test_task_func_with_empty_url():
    url = ""
    with pytest.raises(ValueError) as exc_info:
        task_func(url)
    assert "URL must not be empty." in str(exc_info.value)

def test_task_func_with_invalid_url():
    url = "not_a_valid_url"
    with pytest.raises(urllib.error.URLError) as exc_info:
        task_func(url)
    assert f"Error fetching URL {url}: " in str(exc_info.value)