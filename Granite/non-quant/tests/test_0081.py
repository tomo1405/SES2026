from unittest.mock import patch

from src_0081 import task_func


def test_task_func():
    app = task_func('/path/to/templates')
    assert app.template_folder == '/path/to/templates'

def test_handle_post():
    with task_func('/path/to/templates').app_context():
        data = {'key': 'value'}
        # Mock request.get_json() to return the test data
        with patch('src_0081.request.get_json') as mock_get_json:
            mock_get_json.return_value = data
            # Call the function being tested
            result = handle_post()
            # Assert the expected result
            assert result == 'index.html'
            # Assert that the data was logged
            assert 'data' in caplog.text