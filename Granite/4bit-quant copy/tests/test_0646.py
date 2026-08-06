import os
import pandas as pd
import pytest

from src_0646 import task_func

def test_task_func():
    # Test case 1: File does not exist
    with pytest.raises(FileNotFoundError):
        task_func("nonexistent_file.csv")

    # Test case 2: Empty file
    empty_file = "empty_file.csv"
    with open(empty_file, "w") as f:
        pass
    df = task_func(empty_file)
    assert df.empty

    # Test case 3: Non-empty file
    data = {
        "col1": [1, 2, 3],
        "col2": ["a", "b", "c"]
    }
    non_empty_file = "non_empty_file.csv"
    df = pd.DataFrame(data)
    df.to_csv(non_empty_file, index=False)
    df = task_func(non_empty_file)
    assert not df.empty

    # Clean up
    os.remove(empty_file)
    os.remove(non_empty_file)