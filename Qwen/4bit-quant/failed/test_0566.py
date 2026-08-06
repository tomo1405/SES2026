import pytest
from src_0566 import task_func
import os
import tempfile

def test_task_func():
    # Create a temporary shared library file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.so') as temp_lib:
        temp_lib.write(b'\x7fELF\x01\x01\x01')
        temp_lib.flush()

        # Create a temporary binary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.bin') as temp_bin:
            temp_bin.write(b'example data')
            temp_bin.flush()

            # Test the function
            result = task_func(temp_bin.name)

            # Assert the result is the name of the loaded library
            assert result == os.path.basename(temp_lib.name)

            # Clean up temporary files
            os.unlink(temp_lib.name)
            os.unlink(temp_bin.name)

def test_task_func_with_invalid_file():
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.txt') as temp_txt:
        temp_txt.write('This is a text file.')
        temp_txt.flush()

        # Test the function with an invalid file
        with pytest.raises(OSError):
            task_func(temp_txt.name)

        # Clean up temporary file
        os.unlink(temp_txt.name)