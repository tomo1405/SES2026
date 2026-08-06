import pytest
from src_0714 import task_func

# Mocking os.path.exists to control file existence
class MockPath:
    def __init__(self, exists):
        self.exists = exists

    def exists(self, path):
        return self.exists

def test_task_func_file_not_found(mocker):
    mocker.patch('os.path', new_callable=MockPath, exists=False)
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('nonexistent.log', ['error'])
    assert "Log file nonexistent.log does not exist." in str(excinfo.value)

def test_task_func_no_keywords():
    formatted_lines = task_func('test_log.txt', [])
    assert formatted_lines == []

def test_task_func_empty_log_file(tmp_path):
    log_file = tmp_path / "empty_log.txt"
    log_file.write_text("")
    formatted_lines = task_func(str(log_file), ['error'])
    assert formatted_lines == []

def test_task_func_single_keyword_match(tmp_path):
    log_content = """error 404 Not Found
    warning 500 Internal Server Error
    info User logged in"""
    log_file = tmp_path / "test_log.txt"
    log_file.write_text(log_content)
    formatted_lines = task_func(str(log_file), ['error'])
    expected_output = [
        "      error :             404 :         Not Found"
    ]
    assert formatted_lines == expected_output

def test_task_func_multiple_keywords_match(tmp_path):
    log_content = """error 404 Not Found
    warning 500 Internal Server Error
    info User logged in
    error 502 Bad Gateway"""
    log_file = tmp_path / "test_log.txt"
    log_file.write_text(log_content)
    formatted_lines = task_func(str(log_file), ['error', 'warning'])
    expected_output = [
        "      error :             404 :         Not Found",
        "      error :             502 :       Bad Gateway",
        "    warning :             500 : Internal Server Error"
    ]
    assert formatted_lines == expected_output

def test_task_func_unexpected_line_format(tmp_path):
    log_content = """error 404 Not Found
    warning 500 Internal Server Error
    info User logged in
    unexpected line without spaces"""
    log_file = tmp_path / "test_log.txt"
    log_file.write_text(log_content)
    formatted_lines = task_func(str(log_file), ['error', 'warning'])
    expected_output = [
        "      error :             404 :         Not Found",
        "    warning :             500 : Internal Server Error",
        "Line format unexpected: unexpected line without spaces"
    ]
    assert formatted_lines == expected_output