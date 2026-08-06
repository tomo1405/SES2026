import pytest
from src_0068 import task_func
import os
import re
import pandas as pd

def test_task_func():
    # Create a temporary directory and populate it with test files
    import tempfile
    import shutil

    temp_dir = tempfile.mkdtemp()
    try:
        # Create test files with known sizes
        file_contents = {
            'file1.txt': b'test',
            'file2.txt': b'test',
        }
        for filename, content in file_contents.items():
            with open(os.path.join(temp_dir, filename), 'wb') as f:
                f.write(content)

        # Run the function
        result = task_func(temp_dir)

        # Check the result
        expected_df = pd.DataFrame({
            'File': ['file1.txt', 'file2.txt'],
            'Size': [len(file_contents['file1.txt']),
                      len(file_contents['file2.txt'])]
        })
        pd.testing.assert_frame_equal(result, expected_df)
    finally:
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    pytest.main()