python
import pytest
from src_0720 import task_func

def test_task_func():
    # Test case 1: word is present in a file
    assert task_func('tests/test_files', 'test') == 1
    
    # Test case 2: word is not present in a file
    assert task_func('tests/test_files', 'hello') == 0
    
    # Test case 3: directory does not exist
    with pytest.raises(FileNotFoundError):
        task_func('tests/nonexistent_dir', 'test')
    
    # Test case 4: file is empty
    assert task_func('tests/test_files/empty_file.txt', 'test') == 0
    
    # Test case 5: file is not a text file
    assert task_func('tests/test_files/binary_file.bin', 'test') == 0
    
    # Test case 6: word is present in multiple files
    assert task_func('tests/test_files', 'word') == 2
    
    # Test case 7: word is present in a file with non-ASCII characters
    assert task_func('tests/test_files', 'éàèôî') == 1
    
    # Test case 8: word is present in a file with non-ASCII characters and punctuation
    assert task_func('tests/test_files', 'éàèôî,') == 1
    
    # Test case 9: word is present in a file with non-ASCII characters and uppercase letters
    assert task_func('tests/test_files', 'ÉÀÈÔÎ') == 1
    
    # Test case 10: word is present in a file with non-ASCII characters and uppercase letters and punctuation
    assert task_func('tests/test_files', 'ÉÀÈÔÎ,') == 1