import pytest
from src_0230 import task_func
import os
import json
from datetime import datetime, timedelta

@pytest.fixture
def temp_file_path(tmpdir):
    return str(tmpdir.join("test_log.json"))

def test_task_func_with_seed(temp_file_path):
    seed_value = 42
    num_entries = 5
    task_func(temp_file_path, num_entries, seed=seed_value)

    with open(temp_file_path, 'r') as json_file:
        log_entries = json.load(json_file)

    assert len(log_entries) == num_entries

    for entry in log_entries:
        assert entry['user'] in ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        assert entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
        assert datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')

    # Check that timestamps are in descending order
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S') for entry in log_entries]
    assert timestamps == sorted(timestamps, reverse=True)

def test_task_func_without_seed(temp_file_path):
    num_entries = 5
    task_func(temp_file_path, num_entries)

    with open(temp_file_path, 'r') as json_file:
        log_entries = json.load(json_file)

    assert len(log_entries) == num_entries

    for entry in log_entries:
        assert entry['user'] in ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        assert entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
        assert datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')

    # Check that timestamps are in descending order
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S') for entry in log_entries]
    assert timestamps == sorted(timestamps, reverse=True)

def test_task_func_no_entries(temp_file_path):
    num_entries = 0
    task_func(temp_file_path, num_entries)

    with open(temp_file_path, 'r') as json_file:
        log_entries = json.load(json_file)

    assert len(log_entries) == num_entries

def test_task_func_large_number_of_entries(temp_file_path):
    num_entries = 100
    task_func(temp_file_path, num_entries)

    with open(temp_file_path, 'r') as json_file:
        log_entries = json.load(json_file)

    assert len(log_entries) == num_entries

    for entry in log_entries:
        assert entry['user'] in ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
        assert entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
        assert datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')

    # Check that timestamps are in descending order
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S') for entry in log_entries]
    assert timestamps == sorted(timestamps, reverse=True)

def test_task_func_file_creation(temp_file_path):
    num_entries = 5
    task_func(temp_file_path, num_entries)

    assert os.path.exists(temp_file_path)