import json
import random
from datetime import datetime, timedelta
from src_0230 import task_func
import pytest

USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def test_task_func():
    file_path = 'test_log.json'
    num_entries = 5
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
    expected_output = json.dumps(log_entries, indent=4)
    with open(file_path, 'w') as json_file:
        json.dump(log_entries, json_file, indent=4)
    actual_output = task_func(file_path, num_entries, seed)
    assert actual_output == file_path
    assert open(file_path).read() == expected_output