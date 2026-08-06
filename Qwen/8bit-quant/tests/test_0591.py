import urllib
from datetime import datetime
from unittest.mock import Mock, patch

import pandas as pd
import pytest
from src_0591 import task_func


def test_task_func_empty_url():
    with pytest.raises(ValueError) as excinfo:
        task_func("")
    assert str(excinfo.value) == "URL must not be empty."

@patch('urllib.request.urlopen')
def test_task_func_url_error(mock_urlopen):
    mock_urlopen.side_effect = urllib.error.URLError("Mocked URLError")
    with pytest.raises(urllib.error.URLError) as excinfo:
        task_func("http://example.com")
    assert str(excinfo.value) == "Error fetching URL http://example.com: Mocked URLError"

@patch('urllib.request.urlopen')
def test_task_func_success(mock_urlopen):
    mock_response = Mock()
    mock_response.read.return_value = b"<html><body><a href='link1'>Text1</a><a href='link2'>Text2</a></body></html>"
    mock_urlopen.return_value = mock_response

    expected_df = pd.DataFrame({
        'text': ['Text1', 'Text2'],
        'href': ['link1', 'link2']
    })
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expected_df['fetch_time'] = current_time

    result_df = task_func("http://example.com")

    assert result_df.equals(expected_df)

@patch('urllib.request.urlopen')
def test_task_func_no_links(mock_urlopen):
    mock_response = Mock()
    mock_response.read.return_value = b"<html><body></body></html>"
    mock_urlopen.return_value = mock_response

    expected_df = pd.DataFrame(columns=['text', 'href'])
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    expected_df['fetch_time'] = current_time

    result_df = task_func("http://example.com")

    assert result_df.equals(expected_df)