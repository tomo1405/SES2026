import pytest
from src_0797 import task_func

def test_task_func_no_files(tmpdir):
    # Create an empty directory
    empty_dir = tmpdir.mkdir("empty")
    assert task_func(str(empty_dir)) == []

def test_task_func_no_bracket_files(tmpdir):
    # Create files without brackets
    no_bracket_dir = tmpdir.mkdir("no_brackets")
    no_bracket_dir.join("file1.txt").write("")
    no_bracket_dir.join("file2.py").write("")
    assert task_func(str(no_bracket_dir)) == []

def test_task_func_with_bracket_files(tmpdir):
    # Create files with different types of brackets
    bracket_dir = tmpdir.mkdir("brackets")
    bracket_dir.join("file_(1).txt").write("")
    bracket_dir.join("file{2}.py").write("")
    bracket_dir.join("file[3].csv").write("")
    expected_files = [
        str(bracket_dir.join("file_(1).txt")),
        str(bracket_dir.join("file{2}.py")),
        str(bracket_dir.join("file[3].csv"))
    ]
    assert sorted(task_func(str(bracket_dir))) == sorted(expected_files)

def test_task_func_nested_directories(tmpdir):
    # Create nested directories with files containing brackets
    nested_dir = tmpdir.mkdir("nested")
    sub_dir1 = nested_dir.mkdir("sub1")
    sub_dir2 = nested_dir.mkdir("sub2")
    sub_dir1.join("file_(1).txt").write("")
    sub_dir2.join("file{2}.py").write("")
    expected_files = [
        str(sub_dir1.join("file_(1).txt")),
        str(sub_dir2.join("file{2}.py"))
    ]
    assert sorted(task_func(str(nested_dir))) == sorted(expected_files)

def test_task_func_invalid_directory():
    # Test with an invalid directory path
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_directory")