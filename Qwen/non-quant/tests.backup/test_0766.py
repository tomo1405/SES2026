import pytest
from src_0766 import task_func
import os
from pathlib import Path
import tempfile
import shutil

def test_task_func_no_files():
    result = task_func({})
    assert result == []

def test_task_func_one_non_none_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = Path(temp_dir) / "test_file.txt"
        source_file.write_text("content")
        result = task_func({str(source_file): "content"})
        assert len(result) == 1
        assert Path(result[0]).is_file()
        assert Path(result[0]).name == "test_file.txt"

def test_task_func_multiple_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1 = Path(temp_dir) / "file1.txt"
        file2 = Path(temp_dir) / "file2.txt"
        file3 = Path(temp_dir) / "file3.txt"
        file1.write_text("content1")
        file2.write_text("content2")
        file3.write_text("content3")
        result = task_func({
            str(file1): "content1",
            str(file2): "content2",
            str(file3): None
        })
        assert len(result) == 2
        assert Path(result[0]).is_file()
        assert Path(result[0]).name == "file1.txt"
        assert Path(result[1]).is_file()
        assert Path(result[1]).name == "file2.txt"

def test_task_func_nonexistent_file():
    result = task_func({"nonexistent_file.txt": "content"})
    assert result == []

def test_task_func_target_directory_creation():
    with tempfile.TemporaryDirectory() as temp_dir:
        target_dir = Path(temp_dir) / "custom_target"
        source_file = Path(temp_dir) / "test_file.txt"
        source_file.write_text("content")
        result = task_func({str(source_file): "content"}, target_dir=str(target_dir))
        assert target_dir.is_dir()
        assert len(result) == 1
        assert Path(result[0]).is_file()
        assert Path(result[0]).name == "test_file.txt"

def test_task_func_overwrite_existing_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        source_file = Path(temp_dir) / "test_file.txt"
        source_file.write_text("original_content")
        target_file = Path(temp_dir) / "target_dir" / "test_file.txt"
        target_file.parent.mkdir()
        target_file.write_text("existing_content")
        result = task_func({str(source_file): "content"}, target_dir=str(target_file.parent))
        assert len(result) == 1
        assert Path(result[0]).is_file()
        assert Path(result[0]).read_text() == "original_content"