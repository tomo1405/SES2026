import pytest
from src_1103 import task_func

def test_task_func():
    script_path = "path/to/script.R"
    log_details = task_func(script_path)
    assert log_details["Start Time"] == str(datetime.now())
    assert log_details["End Time"] == str(datetime.now())
    assert log_details["Stdout"] == "expected stdout"
    assert log_details["Stderr"] == "expected stderr"