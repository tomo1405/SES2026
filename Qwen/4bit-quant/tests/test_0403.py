from unittest.mock import patch

from src_0403 import task_func


@patch('requests.get')
@patch('json.loads')
@patch('csv.writer')
@patch('os.path.abspath')
def test_task_func(mock_abspath, mock_csv_writer, mock_json_loads, mock_requests_get):
    # Mocking the API response
    mock_response = mock.Mock()
    mock_response.text = '{"data": ["item1", "item2"]}'
    mock_requests_get.return_value = mock_response

    # Mocking JSON loads
    mock_json_loads.return_value = {'data': ['item1', 'item2']}

    # Mocking CSV writer
    mock_csv_writer.return_value.writerows.return_value = None

    # Mocking file path
    mock_abspath.return_value = '/absolute/path/to/matched_data.csv'

    # Define the pattern to search for
    pattern = r'\d+'

    # Call the function
    result = task_func(pattern)

    # Assertions
    mock_requests_get.assert_called_once_with('https://api.example.com/data')
    mock_json_loads.assert_called_once_with('{"data": ["item1", "item2"]}')
    mock_csv_writer.assert_called_once()
    mock_abspath.assert_called_once_with('matched_data.csv')

    assert result == '/absolute/path/to/matched_data.csv'