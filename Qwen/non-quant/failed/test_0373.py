import pytest
from src_0373 import task_func
import os
from docx import Document

@pytest.fixture
def setup_test_directory(tmpdir):
    # Create a temporary directory with some .docx files
    test_dir = tmpdir.mkdir("test_directory")
    doc1 = test_dir.join("document1.docx")
    doc2 = test_dir.join("document2.docx")
    
    # Create sample .docx files
    doc1.write("")
    doc2.write("")
    
    return str(test_dir)

def test_task_func_no_files(setup_test_directory):
    # Test when there are no .docx files in the directory
    result = task_func(setup_test_directory)
    assert result == 0

def test_task_func_with_files(setup_test_directory):
    # Test when there are .docx files in the directory
    doc1_path = os.path.join(setup_test_directory, "document1.docx")
    doc2_path = os.path.join(setup_test_directory, "document2.docx")
    
    # Add some text to the documents
    doc1 = Document()
    doc1.add_paragraph('This is a "test" document.')
    doc1.save(doc1_path)
    
    doc2 = Document()
    doc2.add_paragraph('Another "example" document.')
    doc2.save(doc2_path)
    
    result = task_func(setup_test_directory)
    assert result == 2
    
    # Check if the files were processed correctly
    processed_doc1 = Document(doc1_path)
    processed_doc2 = Document(doc2_path)
    
    assert processed_doc1.paragraphs[0].text == 'This is a \"test\" document.'
    assert processed_doc2.paragraphs[0].text == 'Another \"example\" document.'

def test_task_func_with_special_characters(setup_test_directory):
    # Test with special characters in the file names
    doc1_path = os.path.join(setup_test_directory, "doc\"ument1.docx")
    doc2_path = os.path.join(setup_test_directory, "doc\"ument2.docx")
    
    # Create the files
    open(doc1_path, 'w').close()
    open(doc2_path, 'w').close()
    
    result = task_func(setup_test_directory)
    assert result == 2