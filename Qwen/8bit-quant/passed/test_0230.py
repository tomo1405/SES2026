import pytest
from src_0230 import task_func
import os
import json
from datetime import datetime, timedelta

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

@pytest.fixture
def temp_file_path(tmpdir):
    return str(tmpdir / "test_log.json")

def test_task_func_output(temp_file_path):
    num_entries = 5
    seed = 42
    file_path = task_func(temp_file_path, num_entries, seed)
    
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as json_file:
        log_entries = json.load(json_file)
    
    assert len(log_entries) == num_entries
    
    for entry in log_entries:
        assert 'user' in entry and entry['user'] in USERS
        assert 'action' in entry and entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
        assert 'timestamp' in entry and isinstance(entry['timestamp'], str)
        
        # Check timestamp format
        try:
            datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            pytest.fail("Timestamp format is incorrect")
    
    # Check that timestamps are in descending order
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S') for entry in log_entries]
    assert timestamps == sorted(timestamps, reverse=True)

def test_task_func_with_no_seed(temp_file_path):
    num_entries = 5
    file_path = task_func(temp_file_path, num_entries)
    
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as json_file:
        log_entries = json.load(json_file)
    
    assert len(log_entries) == num_entries
    
    for entry in log_entries:
        assert 'user' in entry and entry['user'] in USERS
        assert 'action' in entry and entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
        assert 'timestamp' in entry and isinstance(entry['timestamp'], str)
        
        # Check timestamp format
        try:
            datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S')
        except ValueError:
            pytest.fail("Timestamp format is incorrect")
    
    # Check that timestamps are in descending order
    timestamps = [datetime.strptime(entry['timestamp'], '%Y-%m-%dT%H:%M:%S') for entry in log_entries]
    assert timestamps == sorted(timestamps, reverse=True)

def test_task_func_with_zero_entries(temp_file_path):
    num_entries = 0
    seed = 42
    file_path = task_func(temp_file_path, num_entries, seed)
    
    assert os.path.exists(file_path)
    
    with open(file_path, 'r') as json_file:
        log_entries = json.load(json_file)
    
    assert len(log_entries) == num_entries