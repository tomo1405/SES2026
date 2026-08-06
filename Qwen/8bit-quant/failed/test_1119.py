import pytest
from src_1119 import task_func
from unittest.mock import patch, Mock
import os

@pytest.fixture
def mock_csv_response():
    csv_content = "name,age\nAlice,30\nBob,25"
    mock_response = Mock()
    mock_response.text = csv_content
    return mock_response

@patch('requests.get')
@patch('os.path.exists')
def test_task_func(mock_exists, mock_get, mock_csv_response):
    mock_get.return_value = mock_csv_response
    mock_exists.return_value = False  # Ensure file does not exist initially

    json_file_path = task_func(csv_url='https://example.com/data.csv', json_file_path='test_data.json')

    assert os.path.exists(json_file_path)  # Check if the JSON file was created

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        expected_data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"}
        ]
        assert data == expected_data

    os.remove(json_file_path)  # Clean up the created file

@patch('requests.get')
def test_task_func_with_invalid_csv(mock_get):
    mock_get.return_value.text = "invalid,csv,data"

    with pytest.raises(ValueError):
        task_func(csv_url='https://example.com/data.csv', json_file_path='test_data.json')

@patch('requests.get')
def test_task_func_with_empty_csv(mock_get):
    mock_get.return_value.text = ""

    with pytest.raises(ValueError):
        task_func(csv_url='https://example.com/data.csv', json_file_path='test_data.json')