python
import json
import random
from datetime import datetime, timedelta
import pytest

# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    if seed is not None:
        random.seed(seed)
    
    log_entries = []
    current_time = datetime.now()
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'view_page', 'edit_profile', 'post_message'])
        timestamp = current_time.strftime('%Y-%m-%dT%H:%M:%S')
        log_entries.append({'user': user, 'action': action, 'timestamp': timestamp})
        current_time -= timedelta(minutes=random.randint(1, 60))

    with open(file_path, 'w') as json_file:
        json.dump(log_entries, json_file, indent=4)

    return file_path

def test_task_func():
    # Test with default seed
    file_path = 'log.json'
    num_entries = 10
    result = task_func(file_path, num_entries)
    assert result == file_path
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) == num_entries
        for entry in data:
            assert 'user' in entry
            assert 'action' in entry
            assert 'timestamp' in entry

    # Test with custom seed
    file_path = 'log2.json'
    num_entries = 5
    seed = 42
    result = task_func(file_path, num_entries, seed)
    assert result == file_path
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        assert len(data) == num_entries
        for entry in data:
            assert 'user' in entry
            assert 'action' in entry
            assert 'timestamp' in entry

    # Test with invalid seed
    file_path = 'log3.json'
    num_entries = 3
    seed = 'invalid'
    with pytest.raises(TypeError):
        task_func(file_path, num_entries, seed)

    # Test with invalid file path
    file_path = 1234
    num_entries = 2
    with pytest.raises(TypeError):
        task_func(file_path, num_entries)

    # Test with invalid num_entries
    file_path = 'log4.json'
    num_entries = 'invalid'
    with pytest.raises(TypeError):
        task_func(file_path, num_entries)