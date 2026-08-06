import pytest
from src_0642 import task_func

def test_task_func():
    pattern = r"^[a-zA-Z0-9_-]+\.txt$"
    directory = "tests/data"
    output_csv = "tests/output.csv"

    df = task_func(pattern, directory, output_csv)

    assert df.shape[0] == 2
    assert df.shape[1] == 1
    assert df["File Path"][0] == "tests/data/file1.txt"
    assert df["File Path"][1] == "tests/data/file2.txt"