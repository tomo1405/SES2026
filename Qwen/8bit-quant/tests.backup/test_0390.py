import pytest
from src_0390 import task_func
import os
import tempfile
import shutil

@pytest.fixture
def setup_test_directory():
    temp_dir = tempfile.mkdtemp()
    os.makedirs(os.path.join(temp_dir, 'Interesting Files'))
    files = ['example_like.txt', 'test_what.docx', 'uninteresting_file.pdf']
    for file in files:
        with open(os.path.join(temp_dir, file), 'w') as f:
            f.write('Test content')
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func(setup_test_directory):
    directory = setup_test_directory
    result = task_func(directory)
    expected_files = ['example_like.txt', 'test_what.docx']
    assert sorted(result) == sorted(expected_files)
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'example_like.txt'))
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'test_what.docx'))
    assert not os.path.exists(os.path.join(directory, 'uninteresting_file.pdf'))

def test_task_func_no_interesting_files(setup_test_directory):
    directory = setup_test_directory
    # Remove interesting files
    os.remove(os.path.join(directory, 'example_like.txt'))
    os.remove(os.path.join(directory, 'test_what.docx'))
    result = task_func(directory)
    assert result == []
    assert not os.path.exists(os.path.join(directory, 'Interesting Files', 'example_like.txt'))
    assert not os.path.exists(os.path.join(directory, 'Interesting Files', 'test_what.docx'))
    assert os.path.exists(os.path.join(directory, 'uninteresting_file.pdf'))

def test_task_func_empty_directory(setup_test_directory):
    directory = setup_test_directory
    # Remove all files
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))
    result = task_func(directory)
    assert result == []
    assert not os.listdir(os.path.join(directory, 'Interesting Files'))

def test_task_func_case_insensitivity(setup_test_directory):
    directory = setup_test_directory
    # Rename files to test case insensitivity
    os.rename(os.path.join(directory, 'example_like.txt'), os.path.join(directory, 'EXAMPLE_LIKE.TXT'))
    os.rename(os.path.join(directory, 'test_what.docx'), os.path.join(directory, 'TEST_WHAT.DOCX'))
    result = task_func(directory)
    expected_files = ['EXAMPLE_LIKE.TXT', 'TEST_WHAT.DOCX']
    assert sorted(result) == sorted(expected_files)
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'EXAMPLE_LIKE.TXT'))
    assert os.path.exists(os.path.join(directory, 'Interesting Files', 'TEST_WHAT.DOCX'))