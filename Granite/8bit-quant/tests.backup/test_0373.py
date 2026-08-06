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
    directory_path = "/path/to/directory"
    expected_output = 5  # Replace with the expected output for the given directory path
    actual_output = task_func(directory_path)
    assert actual_output == expected_output, "Expected output does not match actual output"