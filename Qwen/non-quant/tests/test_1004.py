import pytest
from src_1004 import task_func
from unittest.mock import patch
import pandas as pd

@patch('urllib.request.urlopen')
def test_task_func_success(mock_urlopen):
    # Mock XML data
    mock_xml_data = b"""
    <root>
        <item>
            <name>Item1</name>
            <value>Value1</value>
        </item>
        <item>
            <name>Item2</name>
            <value>Value2</value>
        </item>
    </root>
    """
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = mock_xml_data

    # Expected DataFrame
    expected_df = pd.DataFrame({
        'name': ['Item1', 'Item2'],
        'value': ['Value1', 'Value2']
    })

    # Call the function
    result_df = task_func('http://example.com/data.xml')

    # Assert the result
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('urllib.request.urlopen')
def test_task_func_empty_items(mock_urlopen):
    # Mock XML data with no items
    mock_xml_data = b"""
    <root>
    </root>
    """
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = mock_xml_data

    # Expect ValueError
    with pytest.raises(ValueError, match="XML structure does not match expected format."):
        task_func('http://example.com/data.xml')

@patch('urllib.request.urlopen')
def test_task_func_invalid_xml(mock_urlopen):
    # Mock invalid XML data
    mock_xml_data = b"<invalid"
    mock_response = mock_urlopen.return_value
    mock_response.read.return_value = mock_xml_data

    # Expect ValueError
    with pytest.raises(ValueError, match="Invalid XML syntax"):
        task_func('http://example.com/data.xml')

@patch('urllib.request.urlopen')
def test_task_func_url_error(mock_urlopen):
    # Simulate URL error
    mock_urlopen.side_effect = Exception("Connection failed")

    # Expect ValueError
    with pytest.raises(ValueError, match="Error fetching the XML file: Connection failed"):
        task_func('http://example.com/data.xml')