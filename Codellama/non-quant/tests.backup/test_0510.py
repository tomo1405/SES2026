import pytest
from src_0510 import task_func


def test_task_func_valid_input():
    file_path1 = "file1.csv"
    file_path2 = "file2.csv"
    delimiter = ","
    quotechar = '"'
    expected_output = pd.DataFrame(
        [[1, "?", "a,b,c"], [2, "?", "d,e,f"], [3, "?", "g,h,i"]],
        columns=["Line Number", "Status", "Content"],
    )
    output = task_func(file_path1, file_path2, delimiter, quotechar)
    pd.testing.assert_frame_equal(output, expected_output)


def test_task_func_invalid_input():
    file_path1 = "file1.csv"
    file_path2 = "file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(ValueError):
        task_func(file_path1, file_path2, delimiter, quotechar)


def test_task_func_empty_file():
    file_path1 = "file1.csv"
    file_path2 = "file2.csv"
    delimiter = ","
    quotechar = '"'
    with pytest.raises(ValueError):
        task_func(file_path1, file_path2, delimiter, quotechar)