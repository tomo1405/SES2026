import csv
import os
import shutil
from datetime import datetime
from random import randint
from unittest.mock import patch, call

from src_0595 import task_func

WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'

def test_task_func():
    hours = 5
    file_path = os.path.join(OUTPUT_DIR, 'weather_data.csv')
    backup_path = os.path.join(OUTPUT_DIR, 'backup/')

    with patch('csv.writer') as mock_writer, patch('os.makedirs') as mock_makedirs, patch('shutil.copy') as mock_copy:
        task_func(hours)

    mock_writer.assert_called()
    mock_makedirs.assert_called_with(backup_path, exist_ok=True)
    mock_copy.assert_has_calls([call(file_path, backup_path)])