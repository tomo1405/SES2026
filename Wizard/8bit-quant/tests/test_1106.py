python
import subprocess
import os
import time
import glob
import pytest

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    # Construct the command to run the R script
    command = f'/usr/bin/Rscript --vanilla {r_script_path}'
    
    # Execute the R script
    subprocess.call(command, shell=True)
    
    # Initialize the start time
    start_time = time.time()
    
    # Construct the search pattern for the output CSV file
    search_pattern = os.path.join(output_path, '*.csv')
    
    # Continuously check if the output file is generated within the specified duration
    while time.time() - start_time < duration:
        if glob.glob(search_pattern):
            return True, 'File generated successfully within the specified duration.'
        time.sleep(0.1)
    
    # Return False with a message if the file is not generated within the specified duration
    return False, 'File not generated within the specified duration.'

def test_task_func():
    # Test case 1: R script runs successfully and generates the output file within the specified duration
    r_script_path = 'test_script.R'
    output_path = 'output'
    duration = 5
    with open(r_script_path, 'w') as f:
        f.write('cat("Hello, world!", file="output.csv")')
    assert task_func(r_script_path, output_path, duration) == (True, 'File generated successfully within the specified duration.')
    os.remove(r_script_path)
    os.remove(os.path.join(output_path, 'output.csv'))
    
    # Test case 2: R script runs successfully but does not generate the output file within the specified duration
    r_script_path = 'test_script.R'
    output_path = 'output'
    duration = 1
    with open(r_script_path, 'w') as f:
        f.write('Sys.sleep(2)')
    assert task_func(r_script_path, output_path, duration) == (False, 'File not generated within the specified duration.')
    os.remove(r_script_path)
    
    # Test case 3: R script fails to run
    r_script_path = 'test_script.R'
    output_path = 'output'
    duration = 5
    with open(r_script_path, 'w') as f:
        f.write('syntax error')
    assert task_func(r_script_path, output_path, duration) == (False, 'File not generated within the specified duration.')
    os.remove(r_script_path)