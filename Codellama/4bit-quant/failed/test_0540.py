import pytest
from src_0540 import task_func

def test_task_func():
    db_name = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    # Test that the function raises a ValueError when num_entries is negative
    with pytest.raises(ValueError):
        task_func(db_name, table_name, -1, random_seed)

    # Test that the function creates a database file with the correct name
    task_func(db_name, table_name, num_entries, random_seed)
    assert os.path.exists(db_name)

    # Test that the function creates a table with the correct name and columns
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"SELECT name, age, height FROM {table_name}")
    columns = [column[0] for column in cur.description]
    assert columns == ["name", "age", "height"]

    # Test that the function inserts the correct number of rows
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    num_rows = cur.fetchone()[0]
    assert num_rows == num_entries

    # Test that the function inserts random data
    cur.execute(f"SELECT name, age, height FROM {table_name} LIMIT 1")
    row = cur.fetchone()
    assert row[0] in NAMES
    assert row[1] in AGES
    assert row[2] in HEIGHTS

    # Test that the function returns the correct path
    assert task_func(db_name, table_name, num_entries, random_seed) == os.path.abspath(db_name)