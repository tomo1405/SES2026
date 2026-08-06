import pytest
from src_1016 import task_func
import os
import pandas as pd
import sqlite3

@pytest.fixture
def mock_webpage_file(tmp_path):
    file_path = tmp_path / "test.html"
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("<html><body><table><tr><td>Row 1 Col 1</td><td>Row 1 Col 2</td></tr><tr><td>Row 2 Col 1</td><td>Row 2 Col 2</td></tr></table></body></html>")
    return f"file://{file_path}"

@pytest.fixture
def mock_webpage_url():
    return "http://example.com"

@pytest.fixture
def mock_database(tmp_path):
    db_path = tmp_path / "test.db"
    return str(db_path)

def test_task_func_with_local_file(mock_webpage_file, mock_database):
    result = task_func(mock_webpage_file, mock_database)
    assert result == 2

    # Check if data is correctly stored in the database
    conn = sqlite3.connect(mock_database)
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    assert len(df) == 2

def test_task_func_with_http_url(mocker, mock_webpage_url, mock_database):
    mock_response = mocker.Mock()
    mock_response.content = b"<html><body><table><tr><td>Row 1 Col 1</td><td>Row 1 Col 2</td></tr><tr><td>Row 2 Col 1</td><td>Row 2 Col 2</td></tr></table></body></html>"
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func(mock_webpage_url, mock_database)
    assert result == 2

    # Check if data is correctly stored in the database
    conn = sqlite3.connect(mock_database)
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    assert len(df) == 2

def test_task_func_empty_data(mock_webpage_file, mock_database):
    empty_html_content = "<html><body><table></table></body></html>"
    with open(mock_webpage_file[7:], "w", encoding="utf-8") as file:
        file.write(empty_html_content)

    result = task_func(mock_webpage_file, mock_database)
    assert result == 0

    # Check if no data is stored in the database
    conn = sqlite3.connect(mock_database)
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    assert df.empty

def test_task_func_request_exception(mocker, mock_webpage_url, mock_database):
    mocker.patch('requests.get', side_effect=requests.RequestException("Test exception"))

    with pytest.raises(requests.RequestException) as excinfo:
        task_func(mock_webpage_url, mock_database)
    assert str(excinfo.value) == "Error accessing URL http://example.com: Test exception"

def test_task_func_database_error(mocker, mock_webpage_file, mock_database):
    def mock_to_sql(*args, **kwargs):
        raise sqlite3.DatabaseError("Test database error")

    mocker.patch('pandas.DataFrame.to_sql', side_effect=mock_to_sql)

    with pytest.raises(sqlite3.DatabaseError) as excinfo:
        task_func(mock_webpage_file, mock_database)
    assert str(excinfo.value) == "Database error with test.db: Test database error"

def test_task_func_cleanup_database(mock_webpage_file, mock_database):
    result = task_func(mock_webpage_file, mock_database)
    assert result == 2

    # Check if the database file is created and then removed
    assert os.path.exists(mock_database)
    os.remove(mock_database)
    assert not os.path.exists(mock_database)