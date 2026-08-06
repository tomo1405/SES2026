import os
import hashlib
import json
from pathlib import Path
from src_1131 import task_func

def test_task_func():
    directory = "/path/to/directory"
    result = task_func(directory)
    assert result == str(Path(directory) / "hashes.json")
    assert os.path.exists(result)
    with open(result) as f:
        hash_dict = json.load(f)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = Path(root) / file
            with open(file_path, "rb") as f:
                bytes = f.read()  # read entire file as bytes
                readable_hash = hashlib.sha256(bytes).hexdigest()
            assert hash_dict[str(file_path)] == readable_hash