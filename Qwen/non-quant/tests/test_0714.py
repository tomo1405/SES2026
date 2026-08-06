import pytest
from src_0714 import task_func
import os
import tempfile

def test_task_func_file_not_found():
    with pytest.raises(FileNotFoundError):
        task_func("non_existent_file.log", ["error"])

def test_task_func_no_keywords():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"INFO user logged in\nERROR user failed login")
        temp_file.close()
        result = task_func(temp_file.name, [])
        assert result == []

def test_task_func_single_keyword_match():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"INFO user logged in\nERROR user failed login")
        temp_file.close()
        result = task_func(temp_file.name, ["ERROR"])
        assert result == ["ERROR          : user failed login"]

def test_task_func_multiple_keywords_match():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"INFO user logged in\nERROR user failed login\nDEBUG system check")
        temp_file.close()
        result = task_func(temp_file.name, ["ERROR", "DEBUG"])
        assert result == ["ERROR          : user failed login", "DEBUG          : system check"]

def test_task_func_unexpected_line_format():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"INFO user logged in\nERROR user failed login\nDEBUG system check invalid")
        temp_file.close()
        result = task_func(temp_file.name, ["ERROR", "DEBUG"])
        assert result == ["ERROR          : user failed login", "Line format unexpected: DEBUG system check invalid"]

def test_task_func_empty_file():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.close()
        result = task_func(temp_file.name, ["ERROR"])
        assert result == []

# Clean up temporary files
for temp_file in [tempfile.NamedTemporaryFile(delete=False), tempfile.NamedTemporaryFile(delete=False)]:
    os.unlink(temp_file.name)