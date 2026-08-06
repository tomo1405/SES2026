import os
from unittest.mock import patch

from src_1138 import task_func


def test_task_func():
    url = "https://www.example.com"
    output_path = "output.json"
    expected_phone_numbers = ["+1234567890", "+9876543210"]

    # Mock the requests.get() function to return a mock response
    with patch("requests.get") as mock_get:
        mock_get.return_value.text = "<html><body>+1234567890</body></html>"
        phone_numbers = task_func(url, output_path)

    assert phone_numbers == expected_phone_numbers
    assert os.path.exists(output_path)
    os.remove(output_path)