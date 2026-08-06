import pytest
from src_0591 import task_func
from unittest.mock import patch
from io import BytesIO
from urllib.error import URLError
import pandas as pd

@patch('src_0591.urllib.request.urlopen')
def test_task_func_valid_url(mock_urlopen):
    # Mock the response
    mock_response = BytesIO(b'<html><body><a href="http://example.com">Example</a></body></html>')
    mock_urlopen.return_value = mock_response

    url = "http://example.com"
    result_df = task_func(url)

    # Check if the DataFrame is correctly formed
    expected_df = pd.DataFrame({
        'text': ['Example'],
        'href': ['http://example.com'],
        'fetch_time': result_df['fetch_time'][0]  # This will be a timestamp, so we compare it directly
    })
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('src_0591.urllib.request.urlopen')
def test_task_func_empty_url(mock_urlopen):
    with pytest.raises(ValueError) as excinfo:
        task_func("")
    assert str(excinfo.value) == "URL must not be empty."

@patch('src_0591.urllib.request.urlopen')
def test_task_func_invalid_url(mock_urlopen):
    mock_urlopen.side_effect = URLError("Mocked URLError")

    url = "http://invalid-url.com"
    with pytest.raises(URLError) as excinfo:
        task_func(url)
    assert str(excinfo.value) == f"Error fetching URL {url}: Mocked URLError"

@patch('src_0591.urllib.request.urlopen')
def test_task_func_no_anchors(mock_urlopen):
    # Mock the response with no anchor tags
    mock_response = BytesIO(b'<html><body>No anchors here</body></html>')
    mock_urlopen.return_value = mock_response

    url = "http://no-anchors.com"
    result_df = task_func(url)

    # Check if the DataFrame is correctly formed with no rows
    expected_df = pd.DataFrame(columns=['text', 'href', 'fetch_time'])
    pd.testing.assert_frame_equal(result_df, expected_df)