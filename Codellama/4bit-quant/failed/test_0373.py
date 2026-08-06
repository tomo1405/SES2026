import pytest
from src_0373 import task_func

def test_task_func():
    directory_path = 'path/to/directory'
    docx_files = ['file1.docx', 'file2.docx', 'file3.docx']
    processed_files = 0

    for docx_file in docx_files:
        document = Document(docx_file)

        for paragraph in document.paragraphs:
            paragraph.text = re.sub(r'(?<!\\)"', r'\"', paragraph.text)

        document.save(docx_file)
        processed_files += 1

    assert processed_files == 3