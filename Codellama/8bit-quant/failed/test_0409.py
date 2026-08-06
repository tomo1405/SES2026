import pytest
from src_0409 import task_func

def test_task_func():
    db_file = "test_db.db"
    query = "SELECT * FROM test_table"
    expected_result = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})

    with sqlite3.connect(db_file) as conn:
        conn.execute("CREATE TABLE test_table (id INTEGER, name TEXT)")
        conn.execute("INSERT INTO test_table VALUES (1, 'Alice')")
        conn.execute("INSERT INTO test_table VALUES (2, 'Bob')")
        conn.execute("INSERT INTO test_table VALUES (3, 'Charlie')")

    result = task_func(db_file, query)

    assert result.equals(expected_result)