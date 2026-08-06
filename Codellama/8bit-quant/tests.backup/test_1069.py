import pytest
from src_1069 import task_func

def test_task_func_valid_input():
    db_path = "test_db.db"
    query = "SELECT * FROM test_table"
    data = task_func(db_path, query)
    assert isinstance(data, pd.DataFrame)
    assert data.shape[0] > 0

def test_task_func_invalid_input():
    db_path = "test_db.db"
    query = "SELECT * FROM invalid_table"
    with pytest.raises(Exception):
        task_func(db_path, query)

def test_task_func_large_dataset():
    db_path = "test_db.db"
    query = "SELECT * FROM test_table"
    data = task_func(db_path, query, warn_large_dataset=True)
    assert isinstance(data, pd.DataFrame)
    assert data.shape[0] > 10000
    assert len(data) > 10000