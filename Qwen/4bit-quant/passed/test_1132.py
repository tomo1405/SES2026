import pytest
from src_1132 import task_func
import sqlite3

# Mocking the database connection and cursor
class MockCursor:
    def __init__(self):
        self.users = [
            (1, 'old_password_1'),
            (2, 'old_password_2')
        ]
        self.executed_queries = []

    def execute(self, query):
        self.executed_queries.append(query)

    def fetchall(self):
        return self.users

    def close(self):
        pass

class MockConnection:
    def __init__(self):
        self.cursor = MockCursor()

    def cursor(self):
        return self.cursor

    def commit(self):
        pass

    def close(self):
        pass

@pytest.fixture
def mock_db():
    return MockConnection()

def test_task_func(mock_db):
    salt = "some_salt"
    cursor = mock_db.cursor
    result = task_func(salt, cursor)

    # Check if the correct number of users were updated
    assert result == len(mock_db.cursor.users)

    # Check if the update queries were executed correctly
    expected_queries = [
        "UPDATE users SET password = '9b74c9897bac770ffc029102a200c5de3b719d9b9d5f1e1e1e1e1e1e1e1e1e1e' WHERE id = 1",
        "UPDATE users SET password = '9b74c9897bac770ffc029102a200c5de3b719d9b9d5f1e1e1e1e1e1e1e1e1e1e' WHERE id = 2"
    ]

    for i, query in enumerate(mock_db.cursor.executed_queries):
        assert query == expected_queries[i]

def test_task_func_type_error():
    with pytest.raises(TypeError):
        task_func(123, None)