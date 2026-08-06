import pytest
from src_0390 import task_func
import os
import shutil
import tempfile

def test_task_func():
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Create some files in the temporary directory
    with open(os.path.join(temp_dir, 'like_this_file.txt'), 'w') as f:
        f.write('This is a test file.')
    with open(os.path.join(temp_dir, 'what_a_day.docx'), 'w') as f:
        f.write('Another test file.')
    with open(os.path.join(temp_dir, 'uninteresting_file.pdf'), 'w') as f:
        f.write('This file should not be moved.')

    # Run the function
    result = task_func(temp_dir)

    # Check that the 'Interesting Files' directory was created
    assert os.path.exists(os.path.join(temp_dir, 'Interesting Files'))

    # Check that the correct files were moved
    expected_files = ['like_this_file.txt', 'what_a_day.docx']
    assert sorted(result) == sorted(expected_files)
    assert not os.path.exists(os.path.join(temp_dir, 'uninteresting_file.pdf'))
    assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'like_this_file.txt'))
    assert os.path.exists(os.path.join(temp_dir, 'Interesting Files', 'what_a_day.docx'))

    # Clean up the temporary directory
    shutil.rmtree(temp_dir)

if __name__ == '__main__':
    pytest.main()