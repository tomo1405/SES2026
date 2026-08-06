python
import pytest
from src_0580 import task_func

def test_task_func_valid_file():
    # Test with a valid file
    ax, most_common_words = task_func('test_data.csv')
    assert ax is not None
    assert most_common_words is not None

def test_task_func_invalid_file():
    # Test with an invalid file
    with pytest.raises(FileNotFoundError):
        task_func('invalid_file.csv')

def test_task_func_empty_file():
    # Test with an empty file
    with open('empty_file.csv', 'w') as file:
        file.write('')
    with pytest.raises(IOError):
        task_func('empty_file.csv')
    # Clean up
    import os
    os.remove('empty_file.csv')