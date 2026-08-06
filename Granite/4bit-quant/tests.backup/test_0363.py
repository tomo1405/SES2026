import pandas as pd
import os
import pytest

from src_0363 import task_func

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func(original_file_location="nonexistent_file.xlsx")

def test_task_func_read_excel_value_error():
    with pytest.raises(ValueError):
        task_func(original_file_location="test.xlsx", sheet_name="InvalidSheet")

def test_task_func_read_write_file():
    original_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    original_file_location = "test.xlsx"
    new_file_location = "new_test.xlsx"
    original_df.to_excel(original_file_location, index=False)
    new_df = task_func(original_file_location=original_file_location, new_file_location=new_file_location)
    assert new_df.equals(original_df)
    os.remove(new_file_location)