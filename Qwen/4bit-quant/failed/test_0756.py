import pytest
from src_0756 import task_func
import tempfile
import shutil

def test_task_func_with_empty_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        result = task_func(temp_dir)
        assert result == []

def test_task_func_with_single_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        initial_filename = 'testfile.txt'
        initial_filepath = os.path.join(temp_dir, initial_filename)
        with open(initial_filepath, 'w') as f:
            f.write('content')
        
        result = task_func(temp_dir)
        expected_new_filename = 'txt.filetest'
        assert result == [expected_new_filename]
        assert os.path.exists(os.path.join(temp_dir, expected_new_filename))
        assert not os.path.exists(initial_filepath)

def test_task_func_with_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        filenames = ['file1.txt', 'file2.docx', 'image.png']
        for filename in filenames:
            filepath = os.path.join(temp_dir, filename)
            with open(filepath, 'w') as f:
                f.write('content')
        
        result = task_func(temp_dir)
        expected_new_filenames = ['txt.file1', 'docx.file2', 'png.image']
        assert set(result) == set(expected_new_filenames)
        for new_filename in expected_new_filenames:
            assert os.path.exists(os.path.join(temp_dir, new_filename))
        for original_filename in filenames:
            assert not os.path.exists(os.path.join(temp_dir, original_filename))

def test_task_func_with_nested_directories():
    with tempfile.TemporaryDirectory() as temp_dir:
        nested_dir = os.path.join(temp_dir, 'subdir')
        os.makedirs(nested_dir)
        initial_filename = 'testfile.txt'
        initial_filepath = os.path.join(nested_dir, initial_filename)
        with open(initial_filepath, 'w') as f:
            f.write('content')
        
        result = task_func(temp_dir)
        assert result == []
        assert os.path.exists(initial_filepath)

def test_task_func_with_nonexistent_directory():
    with pytest.raises(FileNotFoundError):
        task_func('/nonexistent/directory')

def test_task_func_with_readonly_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        initial_filename = 'readonly.txt'
        initial_filepath = os.path.join(temp_dir, initial_filename)
        with open(initial_filepath, 'w') as f:
            f.write('content')
        os.chmod(initial_filepath, 0o444)  # Make file readonly
        
        with pytest.raises(PermissionError):
            task_func(temp_dir)