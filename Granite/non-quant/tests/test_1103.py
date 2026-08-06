import subprocess
import shlex
from datetime import datetime
from src_1103 import task_func
import pytest

def test_task_func():
    script_path = "path/to/script.R"
    log_details = task_func(script_path)
    assert 'Start Time' in log_details
    assert 'End Time' in log_details
    assert 'Stdout' in log_details
    assert 'Stderr' in log_details
    assert isinstance(log_details['Start Time'], str)
    assert isinstance(log_details['End Time'], str)
    assert isinstance(log_details['Stdout'], str)
    assert isinstance(log_details['Stderr'], str)