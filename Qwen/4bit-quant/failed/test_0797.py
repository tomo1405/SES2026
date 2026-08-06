import pytest
from src_0797 import task_func

def test_task_func_with_no_brackets():
    # Create a temporary directory with files that do not contain brackets
    with pytest.tmpdir() as tmpdir:
        tmpdir.join('file1.txt').write('')
        tmpdir.join('file2.py').write('')
        result = task_func(str(tmpdir))
        assert result == []

def test_task_func_with_brackets():
    # Create a temporary directory with files that contain brackets
    with pytest.tmpdir() as tmpdir:
        tmpdir.join('file(1).txt').write('')
        tmpdir.join('file{2}.py').write('')
        tmpdir.join('file[3].md').write('')
        result = task_func(str(tmpdir))
        expected = [
            str(tmpdir.join('file(1).txt')),
            str(tmpdir.join('file{2}.py')),
            str(tmpdir.join('file[3].md'))
        ]
        assert sorted(result) == sorted(expected)

def test_task_func_with_nested_directories():
    # Create a temporary directory with nested directories and files with brackets
    with pytest.tmpdir() as tmpdir:
        sub_dir = tmpdir.mkdir('subdir')
        sub_sub_dir = sub_dir.mkdir('subsubdir')
        sub_dir.join('file(1).txt').write('')
        sub_sub_dir.join('file{2}.py').write('')
        result = task_func(str(tmpdir))
        expected = [
            str(sub_dir.join('file(1).txt')),
            str(sub_sub_dir.join('file{2}.py'))
        ]
        assert sorted(result) == sorted(expected)

def test_task_func_with_empty_directory():
    # Create an empty temporary directory
    with pytest.tmpdir() as tmpdir:
        result = task_func(str(tmpdir))
        assert result == []

def test_task_func_with_non_existent_directory():
    # Test with a non-existent directory
    with pytest.raises(FileNotFoundError):
        task_func('/non/existent/directory')