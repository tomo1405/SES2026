import pytest
from src_1069 import task_func

def test_task_func():
    db_path = "path/to/database.db"
    query = "SELECT * FROM table_name"
    warn_large_dataset = True

    with pytest.warns(UserWarning, match="The data contains more than 10000 rows."):
        data = task_func(db_path, query, warn_large_dataset)

    assert data.shape[0] == 10000

def test_task_func_with_exception():
    db_path = "path/to/database.db"
    query = "SELECT * FROM table_name"
    warn_large_dataset = False

    with pytest.raises(Exception, match="Error fetching data from the database:"):
        task_func(db_path, query, warn_large_dataset)