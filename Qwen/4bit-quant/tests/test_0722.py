import csv

from src_0722 import task_func


def test_task_func_file_not_found():
    result = task_func("non_existent_file.csv")
    assert result is None

def test_task_func_empty_file(tmp_path):
    file_path = tmp_path / "empty_file.csv"
    file_path.touch()
    result = task_func(str(file_path))
    assert result is None

def test_task_func_single_word(tmp_path):
    file_path = tmp_path / "single_word.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['hello'])

    result = task_func(str(file_path))
    assert result == ('hello', 1)

def test_task_func_multiple_words(tmp_path):
    file_path = tmp_path / "multiple_words.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['hello', 'world'])
        writer.writerow(['hello', 'foo'])

    result = task_func(str(file_path))
    assert result == ('hello', 2)

def test_task_func_whitespace_handling(tmp_path):
    file_path = tmp_path / "whitespace.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['  hello  ', 'world  '])
        writer.writerow(['hello', '  world  '])

    result = task_func(str(file_path))
    assert result == ('hello', 2)

def test_task_func_case_insensitivity(tmp_path):
    file_path = tmp_path / "case_insensitivity.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Hello', 'world'])
        writer.writerow(['hello', 'WORLD'])

    result = task_func(str(file_path))
    assert result == ('Hello', 2)