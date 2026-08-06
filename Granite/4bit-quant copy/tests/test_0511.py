import pytest
from src_0511 import task_func

def test_task_func():
    file_path1 = "path/to/file1.gz"
    file_path2 = "path/to/file2.gz"
    expected_output = "List of differences"

    with patch("gzip.open", mock_open(read_data="file1_content\nfile2_content\n")):
        actual_output = task_func(file_path1, file_path2)

    assert actual_output == expected_output