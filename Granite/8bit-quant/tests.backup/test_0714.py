import os
import re
import pytest
from src_0714 import task_func

def test_task_func():
    log_file_path = "path/to/log/file"
    keywords = ["keyword1", "keyword2"]
    expected_output = ["formatted line 1", "formatted line 2", "formatted line 3"]

    with patch("os.path.exists", return_value=True):
        with patch("src_0714.open", mock_open(read_data="line 1\nline 2\nline 3")):
            actual_output = task_func(log_file_path, keywords)
            assert actual_output == expected_output