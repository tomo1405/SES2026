import pytest
from src_0536 import task_func

def test_task_func_positive_num_entries():
    db_path = "test_db.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    assert inserted_rows == num_entries

def test_task_func_negative_num_entries():
    db_path = "test_db.db"
    table_name = "test_table"
    num_entries = -1
    random_seed = 42

    with pytest.raises(ValueError):
        task_func(db_path, table_name, num_entries, random_seed)

def test_task_func_random_seed():
    db_path = "test_db.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    assert inserted_rows == num_entries

    # Re-run the function with the same random seed
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    # The number of inserted rows should be the same as before
    assert inserted_rows == num_entries

def test_task_func_random_seed_different():
    db_path = "test_db.db"
    table_name = "test_table"
    num_entries = 10
    random_seed = 42

    inserted_rows = task_func(db_path, table_name, num_entries, random_seed)

    assert inserted_rows == num_entries

    # Re-run the function with a different random seed
    inserted_rows = task_func(db_path, table_name, num_entries, random_seed + 1)

    # The number of inserted rows should be different
    assert inserted_rows != num_entries