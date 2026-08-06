import os
import pandas as pd
import pytest

from src_0646 import task_func

def test_task_func():
    # Test case 1: File does not exist
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

    # Test case 2: File is empty
    empty_file = "empty_file.csv"
    with open(empty_file, "w") as f:
        pass
    df = task_func(empty_file)
    assert df.empty

    # Test case 3: File contains data
    data = {
        "col1": [1, 2, 3],
        "col2": ["a", "b", "c"]
    }
    data_file = "data_file.csv"
    pd.DataFrame(data).to_csv(data_file, index=False)
    df = task_func(data_file)
    assert df.equals(pd.DataFrame(data))

    # Clean up
    os.remove(empty_file)
    os.remove(data_file)