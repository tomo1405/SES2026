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
    r_script_path = 'path/to/r_script.R'
    output_path = 'path/to/output'
    duration = 10  # in seconds
    
    # Test case 1: File generated successfully within the specified duration
    with patch('subprocess.call') as mock_call, patch('time.time') as mock_time:
        mock_time.return_value = 10  # Set the start time to be 10 seconds ago
        mock_call.return_value = 0  # Simulate successful execution of the R script
        mock_glob = Mock()
        mock_glob.glob.return_value = ['path/to/output/output.csv']  # Simulate the output file being generated
        with patch('glob.glob', mock_glob):
            result = task_func(r_script_path, output_path, duration)
            assert result == (True, 'File generated successfully within the specified duration.')
    
    # Test case 2: File not generated within the specified duration
    with patch('subprocess.call') as mock_call, patch('time.time') as mock_time:
        mock_time.return_value = 10  # Set the start time to be 10 seconds ago
        mock_call.return_value = 0  # Simulate successful execution of the R script
        mock_glob = Mock()
        mock_glob.glob.return_value = []  # Simulate the output file not being generated
        with patch('glob.glob', mock_glob):
            result = task_func(r_script_path, output_path, duration)
            assert result == (False, 'File not generated within the specified duration.')

if __name__ == '__main__':
    pytest.main()