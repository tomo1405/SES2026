import pytest
from src_0709 import task_func
import json
import csv
import os
import base64

def test_task_func():
    raw_string = "eyJhbGciOiJI6ICJodHRwOi8vbG9jYWxob3N0OjgwIiwiYXVkIjoicmVhZGNydW1iZXIiLCJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOiIxMjM0NTY3ODkwIn0="
    filename = "test_file"
    output_dir = "test_output"

    decoded_string = base64.b64decode(raw_string).decode('utf-8')
    data = json.loads(decoded_string)

    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, f'{filename}.csv')

    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])

    assert task_func(raw_string, filename, output_dir) == file_path