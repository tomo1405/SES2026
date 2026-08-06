python
import re
import glob
from docx import Document
import pytest

def task_func(directory_path: str) -> int:
    docx_files = glob.glob(directory_path + '/*.docx')
    processed_files = 0

    for docx_file in docx_files:
        document = Document(docx_file)

        for paragraph in document.paragraphs:
            paragraph.text = re.sub(r'(?<!\\)"', r'\"', paragraph.text)

        document.save(docx_file)
        processed_files += 1

    return processed_files

def test_task_func():
    # Test case 1: directory_path is a valid directory
    directory_path = 'tests/test_files'
    assert task_func(directory_path) == 2

    # Test case 2: directory_path is an invalid directory
    directory_path = 'tests/invalid_directory'
    with pytest.raises(FileNotFoundError):
        task_func(directory_path)

    # Test case 3: directory_path is a file
    directory_path = 'tests/test_files/test_file.txt'
    with pytest.raises(IsADirectoryError):
        task_func(directory_path)