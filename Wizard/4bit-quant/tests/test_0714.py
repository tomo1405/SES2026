python
import os
import re
import pytest

from src_0714 import task_func

def test_task_func_valid_file():
    log_file_path = "test_log.txt"
    with open(log_file_path, "w") as f:
        f.write("INFO : 2021-01-01 : Started the program\n")
        f.write("ERROR : 2021-01-02 : An error occurred\n")
        f.write("INFO : 2021-01-03 : Finished the program\n")

    keywords = ["INFO", "ERROR"]
    formatted_lines = task_func(log_file_path, keywords)

    assert len(formatted_lines) == 2
    assert formatted_lines[0] == "INFO       : 2021-01-01 : Started the program"
    assert formatted_lines[1] == "ERROR      : 2021-01-02 : An error occurred"

    os.remove(log_file_path)

def test_task_func_invalid_file():
    log_file_path = "invalid_log.txt"
    keywords = ["INFO", "ERROR"]

    with pytest.raises(FileNotFoundError):
        task_func(log_file_path, keywords)