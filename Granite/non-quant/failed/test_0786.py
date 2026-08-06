import subprocess
import os
import glob
from src_0786 import task_func

def test_task_func():
    # Test case 1: pattern matches some files
    pattern = '/tmp/archive/*.txt'
    archive_file = task_func(pattern)
    assert archive_file.startswith('/tmp/archive/archive')
    assert archive_file.endswith('.tar.gz')
    assert os.path.exists(archive_file)
    for file in glob.glob(pattern):
        assert not os.path.exists(file)

    # Test case 2: pattern matches no files
    pattern = '/tmp/archive/*.xyz'
    result = task_func(pattern)
    assert result == "No files found matching the pattern."

    # Test case 3: pattern is invalid
    pattern = '/tmp/archive/*.foo'
    with pytest.raises(subprocess.CalledProcessError):
        task_func(pattern)