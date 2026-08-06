import pytest
from src_0572 import task_func
import pandas as pd

def test_task_func():
    f_list = [print, len, sum]
    file_path = "test_file.csv"

    with pytest.raises(ValueError) as exc_info:
        task_func([], file_path)
    assert "f_list should not be empty." in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        task_func(f_list, 123)
    assert "file_path must be a string." in str(exc_info.value)

    with pytest.raises(ValueError) as exc_info:
        task_func(f_list, file_path)
    assert "All elements in f_list must be callable functions." in str(exc_info.value)

    df = pd.read_csv("test_file.csv")
    expected_df = pd.DataFrame({
        "Function Name": ["print", "len", "sum"],
        "Number of Arguments": [1, 1, 1],
        "Defaults": [None, None, None],
        "Annotations": [None, None, None],
        "Is Lambda": [False, False, False]
    })
    assert df.equals(expected_df)