import pytest
from src_1016 import task_func
import os
import pandas as pd
import sqlite3

@pytest.fixture
def temp_file(tmp_path):
    file_path = tmp_path / "test.html"
    file_path.write_text("<html><body><table><tr><td>Row1-Col1</td><td>Row1-Col2</td></tr><tr><td>Row2-Col1</td><td>Row2-Col2</td></tr></table></body></html>")
    return f"file://{file_path}"

@pytest.fixture
def temp_db(tmp_path):
    db_path = tmp_path / "test.db"
    return str(db_path)

def test_task_func_with_file(temp_file, temp_db):
    result = task_func(temp_file, temp_db)
    assert result == 2

    conn = sqlite3.connect(temp_db)
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    assert df.shape == (2, 2)
    assert list(df.columns) == [0, 1]

def test_task_func_with_http(mocker, temp_db):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.content = b"<html><body><table><tr><td>Row1-Col1</td><td>Row1-Col2</td></tr><tr><td>Row2-Col1</td><td>Row2-Col2</td></tr></table></body></html>"
    mocker.patch('requests.get', return_value=mock_response)

    result = task_func("http://example.com", temp_db)
    assert result == 2

    conn = sqlite3.connect(temp_db)
    df = pd.read_sql_query("SELECT * FROM my_table", conn)
    conn.close()
    assert df.shape == (2, 2)
    assert list(df.columns) == [0, 1]

def test_task_func_empty_table(temp_file, temp_db):
    empty_html = "<html><body><table></table></body></html>"
    with open(temp_file[7:], "w", encoding="utf-8") as file:
        file.write(empty_html)

    result = task_func(temp_file, temp_db)
    assert result == 0

    conn = sqlite3.connect(temp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    assert tables == []

def test_task_func_request_exception(mocker, temp_db):
    mocker.patch('requests.get', side_effect=requests.RequestException("Mocked request exception"))

    with pytest.raises(requests.RequestException) as exc_info:
        task_func("http://example.com", temp_db)
    assert "Error accessing URL http://example.com: Mocked request exception" in str(exc_info.value)

def test_task_func_database_error(mocker, temp_file, temp_db):
    mocker.patch('sqlite3.connect', side_effect=sqlite3.DatabaseError("Mocked database error"))

    with pytest.raises(sqlite3.DatabaseError) as exc_info:
        task_func(temp_file, temp_db)
    assert f"Database error with {temp_db}: Mocked database error" in str(exc_info.value)