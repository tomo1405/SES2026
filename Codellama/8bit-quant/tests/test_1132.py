import pytest
from src_1132 import task_func


def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123, None)

def test_task_func_invalid_cursor():
    with pytest.raises(TypeError):
        task_func("salt", 123)

def test_task_func_valid_input():
    cursor = MagicMock()
    cursor.execute.return_value = [
        (1, "password1"),
        (2, "password2"),
        (3, "password3"),
    ]
    count_updated = task_func("salt", cursor)
    assert count_updated == 3
    cursor.execute.assert_called_with("SELECT id, password FROM users")
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 1")
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 2")
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 3")