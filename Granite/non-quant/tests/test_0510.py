import pandas as pd
import pytest
from src_0510 import task_func


def test_task_func():
    file_path1 = "path/to/file1.csv"
    file_path2 = "path/to/file2.csv"
    delimiter = ","
    quotechar = '"'
    expected_df = pd.DataFrame({
        "Line Number": [1, 2, 3],
        "Status": ["!", "@", "#"],
        "Content": ["Row 1 column 1", "Row 2 column 2", "Row 3 column 3"]
    })
    df = task_func(file_path1, file_path2, delimiter, quotechar)
    assert df.equals(expected_df)

def test_task_func_empty_file():
    file_path1 = "path/to/empty_file1.csv"
    file_path2 = "path/to/empty_file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(ValueError) as e:
        task_func(file_path1, file_path2, delimiter, quotechar)
    assert "The file 'path/to/empty_file1.csv' is empty." in str(e.value)

def test_task_func_file_not_found():
    file_path1 = "path/to/file_not_found1.csv"
    file_path2 = "path/to/file_not_found2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(FileNotFoundError) as e:
        task_func(file_path1, file_path2, delimiter, quotechar)
    assert "File not found: The file 'path/to/file_not_found1.csv' does not exist." in str(e.value)

def test_task_func_other_error():
    file_path1 = "path/to/other_error1.csv"
    file_path2 = "path/to/other_error2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(Exception) as e:
        task_func(file_path1, file_path2, delimiter, quotechar)
    assert "Error processing files: Other error message." in str(e.value)