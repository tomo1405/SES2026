import os
import json
from collections import Counter
from unittest.mock import patch, mock_open, MagicMock

def task_func(json_files_path='./json_files/', key='name'):
    key_values = []

    for filename in os.listdir(json_files_path):
        if filename.endswith('.json'):
            file_path = os.path.join(json_files_path, filename)
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                if key in data:
                    key_values.append(data[key])

    return dict(Counter(key_values))