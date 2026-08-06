import pandas as pd
import pytest
from src_0409 import task_func


def test_task_func():
    db_file = "test.db"
    query = "SELECT * FROM test_table"
    expected_result = pd.DataFrame({"id": [1, 2, 3], "name": ["Alice", "Bob", "Charlie"]})

    with pytest.raises(ValueError):
        task_func(db_file, query)

    assert task_func(db_file, query) == expected_result