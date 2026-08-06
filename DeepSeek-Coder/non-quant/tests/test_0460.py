import pytest
from src_0460 import task_func
import subprocess
import os
import time
from datetime import datetime

def test_task_func_valid_input():
    script_dir = "/path/to/scripts"
    scripts = ["script1.sh", "script2.sh"]
    delay = 5

    result = task_func(script_dir, scripts, delay)

    assert isinstance(result, list), "The result should be a list"
    assert len(result) == len(scripts), "The length of the result should be equal to the number of scripts"
    assert all(isinstance(time, str) for time in result), "All elements in the result should be strings"

def test_task_func_invalid_delay():
    script_dir = "/path/to/scripts"
    scripts = ["script1.sh", "script2.sh"]
    delay = -5  # Invalid delay

    with pytest.raises(ValueError):
        task_func(script_dir, scripts, delay)

def test_task_func_no_scripts():
    script_dir = "/path/to/scripts"
    scripts = []
    delay = 5

    with pytest.raises(ValueError):
        task_func(script_dir, scripts, delay)