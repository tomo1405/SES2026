import pytest
from src_1132 import task_func
from unittest.mock import Mock, MagicMock

def test_task_func_with_valid_input():
    # Arrange
    mock_cursor = Mock()
    mock_cursor.fetchall.return_value = [
        (1, 'old_password1'),
        (2, 'old_password2')
    ]
    mock_cursor.execute = MagicMock()

    salt = 'my_salt'

    # Act
    result = task_func(salt, mock_cursor)

    # Assert
    assert result == 2
    mock_cursor.execute.assert_called_with("SELECT id, password FROM users")
    mock_cursor.execute.assert_any_call("UPDATE users SET password = 'e7f6c011776e8db7e3f9b3f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3' WHERE id = 1")
    mock_cursor.execute.assert_any_call("UPDATE users SET password = 'e7f6c011776e8db7e3f9b3f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3f7f3' WHERE id = 2")

def test_task_func_with_invalid_salt_type():
    # Arrange
    mock_cursor = Mock()
    salt = 12345

    # Act & Assert
    with pytest.raises(TypeError):
        task_func(salt, mock_cursor)

def test_task_func_with_no_users():
    # Arrange
    mock_cursor = Mock()
    mock_cursor.fetchall.return_value = []
    mock_cursor.execute = MagicMock()

    salt = 'my_salt'

    # Act
    result = task_func(salt, mock_cursor)

    # Assert
    assert result == 0
    mock_cursor.execute.assert_called_with("SELECT id, password FROM users")
    mock_cursor.execute.assert_not_called("UPDATE users SET password = '...' WHERE id = ...")