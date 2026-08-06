python
import sqlite3
import os
import pytest

from src_0540 import task_func

@pytest.fixture
def db_name():
    return "test.db"

@pytest.fixture
def table_name():
    return "test_table"

@pytest.fixture
def num_entries():
    return 10

@pytest.fixture
def random_seed():
    return 42

def test_task_func(db_name, table_name, num_entries, random_seed):
    task_func(db_name, table_name, num_entries, random_seed)
    assert os.path.exists(db_name)

def test_task_func_invalid_num_entries(db_name, table_name):
    with pytest.raises(ValueError):
        task_func(db_name, table_name, -1)

def test_task_func_invalid_db_name(table_name, num_entries, random_seed):
    with pytest.raises(sqlite3.OperationalError):
        task_func("invalid.db", table_name, num_entries, random_seed)

def test_task_func_invalid_table_name(db_name, num_entries, random_seed):
    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, "invalid_table", num_entries, random_seed)