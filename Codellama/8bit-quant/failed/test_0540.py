import pytest
from src_0540 import task_func

def test_task_func_positive_num_entries():
    db_name = "test_db.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 1234

    result = task_func(db_name, table_name, num_entries, random_seed)

    assert result == os.path.abspath(db_name)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cur.fetchone()[0]

    assert num_rows == num_entries

def test_task_func_negative_num_entries():
    db_name = "test_db.db"
    table_name = "test_table"
    num_entries = -1
    random_seed = 1234

    with pytest.raises(ValueError):
        task_func(db_name, table_name, num_entries, random_seed)

def test_task_func_random_seed():
    db_name = "test_db.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 1234

    result = task_func(db_name, table_name, num_entries, random_seed)

    assert result == os.path.abspath(db_name)

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cur.fetchone()[0]

    assert num_rows == num_entries

    # Check that the data is randomized
    cur.execute(f"SELECT name, age, height FROM {table_name}")
    data = cur.fetchall()
    assert len(data) == num_entries
    assert len(set(data)) == num_entries