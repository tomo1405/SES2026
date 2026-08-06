import json
import random
from datetime import datetime, timedelta
from src_0230 import task_func
import pytest

USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def test_task_func():
    file_path = 'test_log.json'
    num_entries = 10
    seed = 42
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

    result = task_func(file_path, num_entries, seed)

    assert result == 'test_log.json'
    assert os.path.exists(result)
    with open(result) as json_file:
        data = json.load(json_file)
        assert len(data) == num_entries
        for entry in data:
            assert entry['user'] in USERS
            assert entry['action'] in ['login', 'logout', 'view_page', 'edit_profile', 'post_message']
            assert isinstance(entry['timestamp'], str)