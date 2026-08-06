import sqlite3
import numpy as np
from random import choice, seed
from src_0536 import task_func
import pytest

def test_task_func():
    db_path = "path/to/database.db"
    table_name = "people"
    num_entries = 10
    random_seed = 42

    # Setting the random seed if provided
    seed(random_seed)
    np.random.seed(random_seed)

    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = list(range(18, 65))
    HEIGHTS = list(range(150, 200))

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    table_creation_sql = (
        "CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height INTEGER)".format(
            table_name
        )
    )
    cur.execute(table_creation_sql)

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    assert inserted_rows == num_entries, "Number of inserted rows does not match expected value"

    conn.commit()
    conn.close()

if __name__ == "__main__":
    pytest.main()