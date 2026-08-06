import subprocess
import os
import time
import glob
import pytest
from src_1106 import task_func

def test_task_func():
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 10
    
    # Mock the subprocess call to avoid actually running the R script
    with pytest.patch('subprocess.call') as mock_call:
        # Call the function with the given parameters
        result = task_func(r_script_path, output_path, duration)
        
        # Assert that the subprocess call was made with the correct command
        mock_call.assert_called_with(f'/usr/bin/Rscript --vanilla {r_script_path}', shell=True)
        
        # Assert that the function returns the expected result
        assert result == (True, 'File generated successfully within the specified duration.')

def test_task_func_timeout():
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 1
    
    # Mock the subprocess call to avoid actually running the R script
    with pytest.patch('subprocess.call') as mock_call:
        # Mock the time.time() function to simulate a shorter duration
        with pytest.patch('time.time') as mock_time:
            mock_time.side_effect = [0, 1]
            
            # Call the function with the given parameters
            result = task_func(r_script_path, output_path, duration)
            
            # Assert that the subprocess call was made with the correct command
            mock_call.assert_called_with(f'/usr/bin/Rscript --vanilla {r_script_path}', shell=True)
            
            # Assert that the function returns the expected result
            assert result == (False, 'File not generated within the specified duration.')