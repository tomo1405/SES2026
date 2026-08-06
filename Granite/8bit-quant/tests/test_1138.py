from unittest.mock import patch

from src_1138 import task_func


def test_task_func():
    # Test case 1: Test with a URL
    url = "https://www.example.com"
    output_path = "output.json"
    expected_output = ["123-456-7890", "987-654-3210"]
    with patch("src_1138.requests.get") as mock_get, patch("src_1138.json.dump") as mock_json_dump:
        mock_get.return_value.text = "Some HTML content with phone numbers"
        mock_get.return_value.status_code = 200
        result = task_func(url, output_path)
        mock_json_dump.assert_called_once_with(expected_output, open(output_path, "w"))
        assert result == expected_output

    # Test case 2: Test with a local file
    url = "file://path/to/local/file.html"
    output_path = "output.json"
    expected_output = ["123-456-7890", "987-654-3210"]
    with patch("src_1138.open") as mock_open, patch("src_1138.json.dump") as mock_json_dump:
        mock_open.return_value.__enter__.return_value.read.return_value = "Some HTML content with phone numbers"
        result = task_func(url, output_path)
        mock_json_dump.assert_called_once_with(expected_output, open(output_path, "w"))
        assert result == expected_output