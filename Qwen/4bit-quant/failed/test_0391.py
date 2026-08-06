import pytest
from src_0391 import task_func
import pandas as pd
from io import StringIO

# Mocking requests.get to simulate fetching CSV data
class MockResponse:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass

def mock_requests_get(url):
    if url == "http://example.com/data.csv":
        return MockResponse("title,year\nMovie A,2020\nMovie B,2019")
    else:
        raise requests.RequestException("Failed to fetch data")

@pytest.fixture(autouse=True)
def patch_requests(monkeypatch):
    monkeypatch.setattr(requests, 'get', mock_requests_get)

def test_task_func_valid_url():
    csv_url_dict = {"URL": "http://example.com/data.csv"}
    expected_output = pd.DataFrame({"title": ["Movie B", "Movie A"], "year": [2019, 2020]})
    result = task_func(csv_url_dict)
    assert result.equals(expected_output)

def test_task_func_missing_url_key():
    csv_url_dict = {}
    with pytest.raises(ValueError, match="The dictionary must contain a 'URL' key."):
        task_func(csv_url_dict)

def test_task_func_invalid_url():
    csv_url_dict = {"URL": "http://invalid-url.com"}
    with pytest.raises(requests.RequestException, match="Failed to fetch data"):
        task_func(csv_url_dict)

def test_task_func_sort_by_year():
    csv_url_dict = {"URL": "http://example.com/data.csv"}
    expected_output = pd.DataFrame({"title": ["Movie B", "Movie A"], "year": [2019, 2020]})
    result = task_func(csv_url_dict, sort_by_column="year")
    assert result.equals(expected_output)

def test_task_func_nonexistent_sort_column():
    csv_url_dict = {"URL": "http://example.com/data.csv"}
    with pytest.raises(KeyError):
        task_func(csv_url_dict, sort_by_column="nonexistent_column")