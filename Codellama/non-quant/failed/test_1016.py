import pytest
from src_1016 import task_func

def test_task_func_valid_url():
    webpage_url = "https://www.example.com"
    database_name = "my_database.db"
    expected_result = 10

    result = task_func(webpage_url, database_name)

    assert result == expected_result

def test_task_func_invalid_url():
    webpage_url = "https://www.example.com/invalid"
    database_name = "my_database.db"

    with pytest.raises(requests.RequestException):
        task_func(webpage_url, database_name)

def test_task_func_invalid_database():
    webpage_url = "https://www.example.com"
    database_name = "invalid_database.db"

    with pytest.raises(sqlite3.DatabaseError):
        task_func(webpage_url, database_name)