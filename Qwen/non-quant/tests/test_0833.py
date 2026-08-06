import os
import pickle
import tempfile

from src_0833 import task_func


def test_task_func_success():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, 'test_file.pkl')
        data = {'key': 'value'}
        
        # Call the function
        result = task_func(filename, data)
        
        # Check if the function returned True
        assert result is True
        
        # Check if the file was created
        assert os.path.exists(filename)
        
        # Deserialize the file to check the content
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        
        assert loaded_data == data

def test_task_func_failure():
    # Test with a non-writable directory
    filename = '/nonexistent_directory/test_file.pkl'
    data = {'key': 'value'}
    
    # Call the function
    result = task_func(filename, data)
    
    # Check if the function returned False
    assert result is False

def test_task_func_existing_directory():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        filename = os.path.join(temp_dir, 'test_file.pkl')
        data = {'key': 'value'}
        
        # Call the function twice to ensure it handles existing directories
        result1 = task_func(filename, data)
        result2 = task_func(filename, data)
        
        # Check if both calls returned True
        assert result1 is True
        assert result2 is True
        
        # Check if the file was created
        assert os.path.exists(filename)
        
        # Deserialize the file to check the content
        with open(filename, 'rb') as f:
            loaded_data = pickle.load(f)
        
        assert loaded_data == data