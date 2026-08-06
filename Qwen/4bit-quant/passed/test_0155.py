import pytest
from src_0155 import task_func
import os
import tempfile
import glob

def create_temp_files(temp_dir, files):
    for file_name in files:
        with open(os.path.join(temp_dir, file_name), 'w') as f:
            f.write("Sample content")

def test_task_func():
    # Create a temporary directory and some files
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        
        # Create files with different suffixes
        files = [
            "file1.txt",
            "file2.docx",
            "file3.pdf",
            "file4.jpg",
            "file5.png"
        ]
        create_temp_files(temp_dir, files)

        # Test case 1: Pattern matching all files, suffix ".txt"
        result = task_func(temp_dir, "*.txt", r"\.txt$")
        assert result == {"file1.txt": "text/plain"}

        # Test case 2: Pattern matching all files, suffix ".docx"
        result = task_func(temp_dir, "*", r"\.docx$")
        assert result == {"file2.docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"}

        # Test case 3: Pattern matching all files, suffix ".pdf"
        result = task_func(temp_dir, "*", r"\.pdf$")
        assert result == {"file3.pdf": "application/pdf"}

        # Test case 4: Pattern matching all files, suffix ".jpg"
        result = task_func(temp_dir, "*", r"\.jpg$")
        assert result == {"file4.jpg": "image/jpeg"}

        # Test case 5: Pattern matching all files, suffix ".png"
        result = task_func(temp_dir, "*", r"\.png$")
        assert result == {"file5.png": "image/png"}

        # Test case 6: No matching files
        result = task_func(temp_dir, "*.xml", r"\.xml$")
        assert result == {}

        # Test case 7: Empty directory
        os.chdir(temp_dir)
        for file in files:
            os.remove(file)
        result = task_func(temp_dir, "*", r"\.txt$")
        assert result == {}

# Run the tests
if __name__ == "__main__":
    pytest.main()