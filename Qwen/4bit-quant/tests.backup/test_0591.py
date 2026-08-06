import pytest
from src_0591 import task_func
import pandas as pd
from datetime import datetime

def test_task_func_with_valid_url(mocker):
    # Mock the urllib.request.urlopen to return a sample HTML content
    mock_html_content = b'<html><body><a href="https://example.com">Example</a></body></html>'
    mock_response = mocker.Mock()
    mock_response.read.return_value = mock_html_content
    mocker.patch('urllib.request.urlopen', return_value=mock_response)

    # Define the expected DataFrame
    expected_df = pd.DataFrame({
        'text': ['Example'],
        'href': ['https://example.com']
    })
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expected_df['fetch_time'] = [current_time]

    # Call the function
    result_df = task_func('https://example.com')

    # Check if the result matches the expected DataFrame
    pd.testing.assert_frame_equal(result_df, expected_df)

def test_task_func_with_empty_url():
    with pytest.raises(ValueError, match="URL must not be empty."):
        task_func('')

def test_task_func_with_invalid_url(mocker):
    # Mock the urllib.request.urlopen to raise an URLError
    mocker.patch('urllib.request.urlopen', side_effect=urllib.error.URLError('Test error'))

    with pytest.raises(urllib.error.URLError, match="Error fetching URL https://invalid-url.com: Test error"):
        task_func('https://invalid-url.com')