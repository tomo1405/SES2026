import pytest
from src_0208 import task_func
import requests
from unittest.mock import patch

@pytest.mark.parametrize("input_data, expected_endpoint", [
    ("Please visit https://example.com for more info", "https://example.com"),
    ("Check this out: http://another-example.org", "http://another-example.org")
])
def test_task_func_endpoint_extraction(input_data, expected_endpoint):
    with patch('re.search') as mock_search:
        mock_search.return_value.group.return_value = expected_endpoint
        result = task_func(input_data)
        mock_search.assert_called_once_with(r'https?:\/\/[^ ]+', input_data)
        assert result == expected_endpoint

@patch('requests.get')
def test_task_func_response(mock_get):
    mock_response = mock_get.return_value
    mock_response.json.return_value = {"key": "value"}
    input_data = "Visit https://test.com"
    result = task_func(input_data)
    mock_get.assert_called_once_with("https://test.com")
    assert result == {"key": "value"}

@patch('requests.get')
def test_task_func_request_failure(mock_get):
    mock_get.side_effect = requests.RequestException("Connection error")
    input_data = "Visit https://test.com"
    with pytest.raises(requests.RequestException) as excinfo:
        task_func(input_data)
    assert str(excinfo.value) == "Connection error"

@patch('re.search')
def test_task_func_no_url_found(mock_search):
    mock_search.return_value = None
    input_data = "No URL here"
    with pytest.raises(AttributeError) as excinfo:
        task_func(input_data)
    assert str(excinfo.value) == "'NoneType' object has no attribute 'group'"