python
import json
from glob import glob
import pytest

def task_func(directory, string):
    #json_files = list(Path(directory).rglob("/*.json"))
    json_files = glob(f"{directory}/**/*.json", recursive=True)
    found_files = []

    for file in json_files:
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                if string in data:
                    found_files.append(str(file))
        except (IOError, json.JSONDecodeError):
            continue

    return found_files

def test_task_func():
    # Test case 1
    directory = "tests/data"
    string = "hello"
    expected_result = ["tests/data/test.json"]
    assert task_func(directory, string) == expected_result

    # Test case 2
    directory = "tests/data"
    string = "world"
    expected_result = ["tests/data/test.json"]
    assert task_func(directory, string) == expected_result

    # Test case 3
    directory = "tests/data"
    string = "foo"
    expected_result = []
    assert task_func(directory, string) == expected_result