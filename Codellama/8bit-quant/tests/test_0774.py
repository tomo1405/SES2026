import os
import re

from src_0774 import task_func


def test_task_func():
    # Setup
    source_dir = '/source/dir'
    target_dir = '/target/dir'
    file_pattern = re.compile(r'^(.*?)-\d+\.json$')
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    for i in range(5):
        filename = f'file{i}.json'
        with open(os.path.join(source_dir, filename), 'w') as f:
            f.write('{}')
    # Test
    task_func()
    # Assertions
    for filename in os.listdir(source_dir):
        assert not os.path.exists(os.path.join(source_dir, filename))
    for filename in os.listdir(target_dir):
        assert os.path.exists(os.path.join(target_dir, filename))