import pytest
from unittest.mock import patch, MagicMock
from src_1119 import task_func

@pytest.fixture
def mock_response():
    mock_csv_data = """name,age,city
Alice,30,New York
Bob,25,Los Angeles"""
    mock_response = MagicMock()
    mock_response.text = mock_csv_data
    return mock_response

@patch('requests.get')
@patch('builtins.open', new_callable=MagicMock)
def test_task_func(mock_open, mock_get, mock_response):
    mock_get.return_value = mock_response
    expected_json_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"}
    ]
    expected_json_file_path = 'data.json'

    result = task_func()

    assert result == expected_json_file_path
    mock_get.assert_called_once_with(CSV_URL)
    mock_open.assert_called_once_with(expected_json_file_path, 'w')
    mock_open().write.assert_called_once_with(
        json.dumps(expected_json_data, indent=None, separators=(',', ':'))
    )