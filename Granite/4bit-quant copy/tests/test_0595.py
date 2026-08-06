import csv
import os
import shutil
from datetime import datetime
from random import randint
from src_0595 import task_func
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'

def test_task_func():
    hours = 5
    file_path = task_func(hours)
    assert os.path.exists(file_path)
    with open(file_path, 'r', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) == hours + 1  # +1 for the header row
        for row in data[1:]:  # skip the header row
            assert len(row) == 2
            time, condition = row
            assert datetime.strptime(time, '%H:%M:%S.%f')
            assert condition in WEATHER_CONDITIONS
    backup_path = os.path.join(OUTPUT_DIR, 'backup/')
    assert os.path.exists(backup_path)
    assert os.path.exists(os.path.join(backup_path, os.path.basename(file_path)))