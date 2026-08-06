import csv
import os
import shutil
from datetime import datetime
from random import randint
from unittest.mock import patch, call

from src_0595 import task_func

WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'
FILE_PATH = os.path.join(OUTPUT_DIR, 'weather_data.csv')
BACKUP_PATH = os.path.join(OUTPUT_DIR, 'backup/')

def test_task_func():
    with patch('csv.writer') as mock_writer, patch('os.makedirs') as mock_makedirs, patch('shutil.copy') as mock_copy:
        hours = randint(1, 100)
        data = [['Time', 'Condition']]
        for i in range(hours):
            row = [datetime.now().strftime('%H:%M:%S.%f'), WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS)-1)]]
            data.append(row)

        task_func(hours)

        mock_writer.assert_called_once()
        mock_makedirs.assert_called_once_with(BACKUP_PATH, exist_ok=True)
        mock_copy.assert_has_calls([
            call(FILE_PATH, BACKUP_PATH),
        ])