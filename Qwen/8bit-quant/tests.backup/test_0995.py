import pytest
from unittest.mock import patch, MagicMock
from src_0995 import task_func

@pytest.fixture
def mock_response():
    response = MagicMock()
    response.status_code = 200
    response.text = """
    <html>
        <div class="container">
            <h1>Title 1</h1>
            <span class="date">2023-01-01</span>
            <span class="author">Author 1</span>
        </div>
        <div class="container">
            <h1>Title 2</h1>
            <span class="date">2023-01-02</span>
            <span class="author">Author 2</span>
        </div>
    </html>
    """
    return response

@patch('requests.get')
@patch('pandas.DataFrame.to_csv')
def test_task_func(mock_to_csv, mock_get, mock_response, tmpdir):
    mock_get.return_value = mock_response

    url = "http://example.com"
    csv_file_path = str(tmpdir.join("test.csv"))

    result = task_func(url, csv_file_path)

    expected_data = [
        ("Title 1", "2023-01-01", "Author 1"),
        ("Title 2", "2023-01-02", "Author 2")
    ]

    assert result == expected_data
    mock_to_csv.assert_called_once_with(csv_file_path, index=False)

@patch('requests.get')
def test_task_func_request_exception(mock_get):
    mock_get.side_effect = requests.RequestException("Connection error")

    url = "http://example.com"
    csv_file_path = "test.csv"

    with pytest.raises(RuntimeError) as excinfo:
        task_func(url, csv_file_path)

    assert "Error fetching URL: Connection error" in str(excinfo.value)

@patch('requests.get')
def test_task_func_no_data_found(mock_get, mock_response):
    mock_get.return_value = mock_response
    mock_response.text = "<html></html>"

    url = "http://example.com"
    csv_file_path = "test.csv"

    result = task_func(url, csv_file_path)

    expected_data = [("No Title", "No Date", "No Author")]

    assert result == expected_data