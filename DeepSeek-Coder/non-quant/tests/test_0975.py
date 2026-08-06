import pytest
from src_0975 import task_func
import pathlib
import shutil

def test_task_func():
    # Create a temporary directory for testing
    test_dir = pathlib.Path('test_dir')
    test_dir.mkdir()
    test_file = test_dir / 'test_file.txt'
    test_file.write_text('test content')

    # Call the function
    result = task_func(str(test_dir), str(test_dir))

    # Assertions
    assert result == (test_dir.name, ['test_file.txt'])

    # Clean up
    shutil.rmtree(str(test_dir))