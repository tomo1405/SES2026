import pytest
from src_0603 import task_func
import os
import numpy as np
import pandas as pd

@pytest.fixture
def setup():
    # Setup code before each test
    pass

def test_task_func(setup):
    # Test the function
    file_path = 'test_file.csv'
    output_dir = './output'
    task_func(file_path, output_dir=output_dir)
    
    # Add assertions to verify the output
    assert os.path.exists(file_path), "File not created"
    assert os.path.isfile(file_path), "File not created"
    os.remove(file_path)  # Clean up