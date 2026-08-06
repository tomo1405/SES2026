import pytest
from src_1132 import task_func


def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123, None)

def test_task_func_return_value():
    cursor = MagicMock()
    cursor.execute.return_value = [
        (1, 'password1'),
        (2, 'password2'),
        (3, 'password3')
    ]
    assert task_func('salt', cursor) == 3

def test_task_func_update_password():
    cursor = MagicMock()
    cursor.execute.return_value = [
        (1, 'password1'),
        (2, 'password2'),
        (3, 'password3')
    ]
    task_func('salt', cursor)
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 1")
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 2")
    cursor.execute.assert_called_with("UPDATE users SET password = 'hashed_password' WHERE id = 3")