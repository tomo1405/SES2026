import pytest
from src_1106 import task_func
import os
import time
import glob
import tempfile

def test_task_func_success():
    with tempfile.TemporaryDirectory() as temp_dir:
        r_script_path = os.path.join(temp_dir, "test_script.R")
        output_path = os.path.join(temp_dir, "output")
        os.makedirs(output_path)
        
        # Create a simple R script that writes a CSV file
        with open(r_script_path, 'w') as f:
            f.write('write.csv(data.frame(a=1,b=2), file="output/test_output.csv")')
        
        # Call the function
        result, message = task_func(r_script_path, output_path, 5)
        
        # Assert the results
        assert result == True
        assert message == 'File generated successfully within the specified duration.'
        assert os.path.exists(os.path.join(output_path, "test_output.csv"))

def test_task_func_failure():
    with tempfile.TemporaryDirectory() as temp_dir:
        r_script_path = os.path.join(temp_dir, "non_existent_script.R")
        output_path = os.path.join(temp_dir, "output")
        os.makedirs(output_path)
        
        # Call the function
        result, message = task_func(r_script_path, output_path, 1)
        
        # Assert the results
        assert result == False
        assert message == 'File not generated within the specified duration.'

def test_task_func_timeout():
    with tempfile.TemporaryDirectory() as temp_dir:
        r_script_path = os.path.join(temp_dir, "test_script.R")
        output_path = os.path.join(temp_dir, "output")
        os.makedirs(output_path)
        
        # Create a simple R script that does nothing
        with open(r_script_path, 'w') as f:
            f.write('')
        
        # Call the function
        result, message = task_func(r_script_path, output_path, 1)
        
        # Assert the results
        assert result == False
        assert message == 'File not generated within the specified duration.'