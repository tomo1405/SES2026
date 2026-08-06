import os

import pytest
from src_0732 import task_func


def test_task_func():
    # Call the function
    loaded_data, loaded_target = task_func(DATA, TARGET)
    
    # Check if the loaded data and target match the original
    assert (loaded_data == DATA).all()
    assert (loaded_target == TARGET).all()
    
    # Check if the file was deleted
    assert not os.path.exists(FILE_NAME)

    # Check if the function correctly handles the file operations
    with pytest.raises(FileNotFoundError):
        with open(FILE_NAME, 'rb') as file:
            pass