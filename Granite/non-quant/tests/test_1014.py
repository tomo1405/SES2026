import pytest
import requests
from src_1014 import task_func


def test_task_func():
    # Test case 1: Test with valid URL and default base_url and csv_file
    result = task_func("https://www.example.com")
    assert result > 0

    # Test case 2: Test with valid URL, custom base_url and csv_file
    result = task_func("https://www.example.com", "https://www.example.org", "scraped_data_2.csv")
    assert result > 0
    assert "scraped_data_2.csv"

    # Test case 3: Test with invalid URL and default base_url and csv_file
    with pytest.raises(requests.exceptions.RequestException):
        task_func("https://www.invalid-url.com")