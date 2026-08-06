python
import pytest
from src_0778 import task_func

def test_task_func():
    directory = 'test_directory'
    os.makedirs(directory, exist_ok=True)
    # Create some zip files in the directory
    for i in range(5):
        with open(os.path.join(directory, f'file-{i}.zip'), 'w') as f:
            f.write('test')
    # Call the function and check the result
    extracted_dirs = task_func(directory)
    assert len(extracted_dirs) == 5
    for i in range(5):
        assert os.path.exists(os.path.join(directory, f'file-{i}'))