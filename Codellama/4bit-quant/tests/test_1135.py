import pytest
from src_1135 import task_func

def test_task_func():
    source_dir = 'tests/test_data/source'
    target_dir = 'tests/test_data/target'
    prefix = '#Hash: '
    
    new_files = task_func(source_dir, target_dir, prefix)
    
    assert len(new_files) == 2
    assert os.path.exists(new_files[0])
    assert os.path.exists(new_files[1])
    
    with open(new_files[0], 'r') as infile:
        content = infile.read()
    
    assert content.startswith(prefix)
    assert len(content) > len(prefix)
    
    with open(new_files[1], 'r') as infile:
        content = infile.read()
    
    assert content.startswith(prefix)
    assert len(content) > len(prefix)