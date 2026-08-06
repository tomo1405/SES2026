import subprocess
import os
import time
import glob
import pytest
from src_1106 import task_func

def test_task_func():
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 10  # Specify the desired duration in seconds
    
    # Call the function with the provided arguments
    result = task_func(r_script_path, output_path, duration)
    
    # Assert that the function returns True and a success message
    assert result[0] is True
    assert 'File generated successfully within the specified duration.' in result[1]
    
    # Wait for the specified duration plus some buffer time to ensure the function has been executed
    time.sleep(duration + 1)
    
    # Call the function again to check if it returns False and an error message
    result = task_func(r_script_path, output_path, duration)
    
    # Assert that the function returns False and an error message
    assert result[0] is False
    assert 'File not generated within the specified duration.' in result[1]