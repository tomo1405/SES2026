import sys

from src_0993 import task_func


def test_task_func():
    path_to_append = "test_path"
    database = "test_database.db"
    result = task_func(path_to_append, database)
    assert result == path_to_append
    assert "test_path" in sys.path
    assert "test_database.db" == DATABASE