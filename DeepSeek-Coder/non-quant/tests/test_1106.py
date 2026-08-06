import pytest
from src_1106 import task_func
import subprocess
import os
import time
import glob

@pytest.fixture
def setup_and_teardown():
    # Setup code here if needed
    pass

def test_task_func_success(setup_and_teardown):
    # Test the function with a successful outcome
    result = task_func('path/to/r_script.R', 'path/to/output', 5)
    assert result == (True, 'File generated successfully within the specified duration.')

def test_task_func_failure(setup_and_teardown):
    # Test the function with a failure outcome
    result = task_func('path/to/r_script.R', 'path/to/output', 1)
    assert result == (False, 'File not generated within the specified duration.')