import hashlib
import binascii
from src_1132 import task_func
import pytest

def test_task_func():
    # Test case 1: salt is not a string
    with pytest.raises(TypeError):
        task_func(123, None)

    # Test case 2: salt is a string, but cursor is None
    with pytest.raises(TypeError):
        task_func("abc", None)

    # Test case 3: valid input, no updates expected
    mock_cursor = MockCursor()
    mock_cursor.fetchall.return_value = []
    result = task_func("abc", mock_cursor)
    assert result == 0

    # Test case 4: valid input, updates expected
    mock_cursor = MockCursor()
    mock_cursor.fetchall.return_value = [(1, "password1"), (2, "password2")]
    result = task_func("abc", mock_cursor)
    assert result == 2
    mock_cursor.execute.assert_has_calls([
        call("SELECT id, password FROM users"),
        call("UPDATE users SET password = '5e4b907a51e67b50a66ae6351e75545f65f31f419c51d04d9f398716e8d2b666' WHERE id = 1"),
        call("UPDATE users SET password = '098f6bcd4621d373cade4e832627b4f6' WHERE id = 2")
    ])

class MockCursor:
    def __init__(self):
        self.execute_calls = []

    def execute(self, sql):
        self.execute_calls.append(sql)

    def fetchall(self):
        return []