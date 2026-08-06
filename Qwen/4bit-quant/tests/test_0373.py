import os
import tempfile

from src_0373 import task_func


def create_temp_docx(file_path, content):
    doc = Document()
    doc.add_paragraph(content)
    doc.save(file_path)

def test_task_func_with_no_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == 0

def test_task_func_with_one_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.docx')
        create_temp_docx(file_path, 'Hello "World"')
        result = task_func(temp_dir)
        assert result == 1
        with open(file_path, 'rb') as f:
            doc = Document(f)
            assert doc.paragraphs[0].text == 'Hello \"World\"'

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path1 = os.path.join(temp_dir, 'test1.docx')
        file_path2 = os.path.join(temp_dir, 'test2.docx')
        create_temp_docx(file_path1, 'Hello "World"')
        create_temp_docx(file_path2, 'Another "Example"')
        result = task_func(temp_dir)
        assert result == 2
        with open(file_path1, 'rb') as f:
            doc1 = Document(f)
            assert doc1.paragraphs[0].text == 'Hello \"World\"'
        with open(file_path2, 'rb') as f:
            doc2 = Document(f)
            assert doc2.paragraphs[0].text == 'Another \"Example\"'

def test_task_func_with_special_characters():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, 'test.docx')
        create_temp_docx(file_path, 'Special "Characters: " & \'Quotes\'')
        result = task_func(temp_dir)
        assert result == 1
        with open(file_path, 'rb') as f:
            doc = Document(f)
            assert doc.paragraphs[0].text == 'Special \"Characters: \" & \'Quotes\''