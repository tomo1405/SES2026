from unittest.mock import Mock, call

from src_1132 import task_func


def test_task_func():
    # Mock the cursor object
    mock_cursor = Mock()
    # Set up the expected SQL queries and responses
    mock_cursor.execute.side_effect = [
        # First call to execute is to get the list of users
        [
            (1, 'password1'),
            (2, 'password2')
        ],
        # Second call to execute is to update the passwords
        None
    ]

    # Call the function with the mock cursor
    result = task_func('salt', mock_cursor)

    # Assert that the expected SQL queries were called
    assert mock_cursor.execute.call_count == 2
    assert mock_cursor.execute.call_args_list == [
        call("SELECT id, password FROM users"),
        call("UPDATE users SET password = '...WHERE id = 1"),
        call("UPDATE users SET password = '...WHERE id = 2"),
    ]

    # Assert that the function returned the expected result
    assert result == 2