import pytest
from src_0538 import task_func
import pandas as pd
import sqlite3

def test_task_func_with_valid_data():
    # Create a temporary SQLite database and populate it with valid data
    db_name = ":memory:"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (age INTEGER)")
    cursor.execute("INSERT INTO People VALUES (25), (30), (35)")
    conn.commit()
    conn.close()

    # Call the function
    ax = task_func(db_name=db_name, table_name="People")

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_negative_age():
    # Create a temporary SQLite database and populate it with invalid data (negative age)
    db_name = ":memory:"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (age INTEGER)")
    cursor.execute("INSERT INTO People VALUES (-1), (30), (35)")
    conn.commit()
    conn.close()

    # Expect a ValueError to be raised
    with pytest.raises(ValueError, match="Data contains negative age values."):
        task_func(db_name=db_name, table_name="People")

def test_task_func_with_empty_table():
    # Create a temporary SQLite database and populate it with no data
    db_name = ":memory:"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE People (age INTEGER)")
    conn.commit()
    conn.close()

    # Call the function
    ax = task_func(db_name=db_name, table_name="People")

    # Check if the returned object is a matplotlib AxesSubplot
    assert isinstance(ax, sns.axisgrid.FacetGrid)

def test_task_func_with_nonexistent_table():
    # Create a temporary SQLite database without the specified table
    db_name = ":memory:"
    conn = sqlite3.connect(db_name)
    conn.close()

    # Expect a sqlite3.OperationalError to be raised
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name=db_name, table_name="NonExistentTable")