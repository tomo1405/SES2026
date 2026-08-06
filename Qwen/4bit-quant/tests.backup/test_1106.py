import pytest
from src_1106 import task_func
import os
import time
import glob
import subprocess

def test_task_func_success(tmpdir):
    # Create a temporary directory for the R script and output path
    r_script_path = tmpdir.join("test_script.R").strpath
    output_path = tmpdir.join("output").strpath
    os.makedirs(output_path)

    # Write a simple R script that creates a CSV file
    with open(r_script_path, "w") as f:
        f.write('write.csv(data.frame(x=1, y=2), file="{}")'.format(os.path.join(output_path, "test_output.csv")))

    # Call the function with a duration that should be sufficient for the script to run
    result = task_func(r_script_path, output_path, 5)
    assert result == (True, 'File generated successfully within the specified duration.')

def test_task_func_failure(tmpdir):
    # Create a temporary directory for the R script and output path
    r_script_path = tmpdir.join("test_script.R").strpath
    output_path = tmpdir.join("output").strpath
    os.makedirs(output_path)

    # Write a simple R script that does nothing
    with open(r_script_path, "w") as f:
        f.write('# This script does nothing')

    # Call the function with a very short duration to ensure failure
    result = task_func(r_script_path, output_path, 1)
    assert result == (False, 'File not generated within the specified duration.')

def test_task_func_invalid_r_script_path():
    # Use an invalid path for the R script
    r_script_path = "/nonexistent/path/to/script.R"
    output_path = "/nonexistent/path/to/output"
    
    # Call the function with a duration that should be sufficient for the script to run
    result = task_func(r_script_path, output_path, 5)
    assert result == (False, 'File not generated within the specified duration.')

def test_task_func_invalid_output_path(tmpdir):
    # Create a temporary directory for the R script
    r_script_path = tmpdir.join("test_script.R").strpath
    
    # Write a simple R script that creates a CSV file
    with open(r_script_path, "w") as f:
        f.write('write.csv(data.frame(x=1, y=2), file="{}")'.format("/nonexistent/path/to/test_output.csv"))

    # Call the function with a very short duration to ensure failure
    result = task_func(r_script_path, "/nonexistent/path/to/output", 5)
    assert result == (False, 'File not generated within the specified duration.')