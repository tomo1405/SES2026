import pytest
from src_0744 import task_func

def test_task_func_no_json_files(tmpdir):
    # Create a temporary directory with no JSON files
    assert task_func(str(tmpdir)) == {"is_": 0, "has_": 0, "can_": 0, "should_": 0}

def test_task_func_single_json_file(tmpdir):
    # Create a temporary directory with one JSON file
    json_content = '{"is_valid": true, "has_data": false}'
    json_file = tmpdir.join("data.json")
    json_file.write(json_content)

    expected_stats = {"is_": 1, "has_": 1, "can_": 0, "should_": 0}
    assert task_func(str(tmpdir)) == expected_stats

def test_task_func_multiple_json_files(tmpdir):
    # Create a temporary directory with multiple JSON files
    json_content_1 = '{"is_valid": true, "has_data": false, "can_process": true}'
    json_content_2 = '{"should_run": true, "has_data": true}'
    json_file_1 = tmpdir.join("data1.json")
    json_file_2 = tmpdir.join("data2.json")
    json_file_1.write(json_content_1)
    json_file_2.write(json_content_2)

    expected_stats = {"is_": 1, "has_": 2, "can_": 1, "should_": 1}
    assert task_func(str(tmpdir)) == expected_stats

def test_task_func_empty_json_file(tmpdir):
    # Create a temporary directory with an empty JSON file
    json_content = '{}'
    json_file = tmpdir.join("empty.json")
    json_file.write(json_content)

    expected_stats = {"is_": 0, "has_": 0, "can_": 0, "should_": 0}
    assert task_func(str(tmpdir)) == expected_stats

def test_task_func_non_json_file(tmpdir):
    # Create a temporary directory with a non-JSON file
    text_content = "This is a text file."
    text_file = tmpdir.join("data.txt")
    text_file.write(text_content)

    expected_stats = {"is_": 0, "has_": 0, "can_": 0, "should_": 0}
    assert task_func(str(tmpdir)) == expected_stats

def test_task_func_nested_json_keys(tmpdir):
    # Create a temporary directory with a JSON file containing nested keys
    json_content = '{"is_valid": {"nested": true}, "has_data": false}'
    json_file = tmpdir.join("nested.json")
    json_file.write(json_content)

    expected_stats = {"is_": 1, "has_": 1, "can_": 0, "should_": 0}
    assert task_func(str(tmpdir)) == expected_stats