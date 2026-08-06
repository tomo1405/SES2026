import pytest
from src_0724 import task_func

def test_task_func():
    url = "https://example.com"
    expected_output = "scraped_data.csv"
    actual_output = task_func(url)
    assert actual_output == expected_output, "Expected output does not match actual output"

def test_task_func_with_invalid_url():
    url = "https://invalid-url"
    with pytest.raises(Exception) as e:
        task_func(url)
    assert "urllib.error.URLError" in str(e), "Expected exception type not raised"