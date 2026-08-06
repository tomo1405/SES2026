import os
import pickle
import tempfile

from src_0833 import task_func


def test_task_func_success():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "test_data.pkl")
        data = {"key": "value"}
        
        # Call the function
        result = task_func(filename, data)
        
        # Check if the function returns True
        assert result is True
        
        # Check if the file was created
        assert os.path.exists(filename)
        
        # Deserialize the data to check if it matches
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        assert loaded_data == data

def test_task_func_failure():
    # Use an invalid filename (e.g., a read-only directory)
    filename = "/root/test_data.pkl"
    data = {"key": "value"}
    
    # Call the function
    result = task_func(filename, data)
    
    # Check if the function returns False
    assert result is False

def test_task_func_existing_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, "subdir", "test_data.pkl")
        data = {"key": "value"}
        
        # Call the function
        result = task_func(filename, data)
        
        # Check if the function returns True
        assert result is True
        
        # Check if the file was created
        assert os.path.exists(filename)
        
        # Deserialize the data to check if it matches
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        assert loaded_data == data