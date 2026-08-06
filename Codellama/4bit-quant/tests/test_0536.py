import pytest
from src_0536 import task_func

def test_task_func():
    # Test case 1: num_entries = 0
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 0
    random_seed = None
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 0

    # Test case 2: num_entries = 1
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 1
    random_seed = None
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 1

    # Test case 3: num_entries = 10
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = None
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 10

    # Test case 4: num_entries = 100
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 100
    random_seed = None
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 100

    # Test case 5: num_entries = -1
    db_path = "test.db"
    table_name = "test_table"
    num_entries = -1
    random_seed = None
    with pytest.raises(ValueError):
        task_func(db_path, table_name, num_entries, random_seed)

    # Test case 6: random_seed = 1234
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 1234
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 10

    # Test case 7: random_seed = 4321
    db_path = "test.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 4321
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)
    assert inserted_rows == 10