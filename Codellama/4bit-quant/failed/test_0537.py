import pytest
from src_0537 import task_func

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    csv_path = "test_data.csv"
    expected_path = os.path.abspath(csv_path)

    with pytest.raises(sqlite3.OperationalError):
        task_func(db_name, table_name, csv_path)

    assert os.path.exists(expected_path)
    assert os.path.isfile(expected_path)
    assert os.path.getsize(expected_path) > 0

    os.remove(expected_path)