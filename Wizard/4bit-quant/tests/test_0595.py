python
import csv
import os
import shutil
from datetime import datetime
from random import randint
import pytest

# Constants
WEATHER_CONDITIONS = ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']
OUTPUT_DIR = './output'

def task_func(hours, output_dir=OUTPUT_DIR):
    FILE_PATH = os.path.join(output_dir, 'weather_data.csv')
    BACKUP_PATH = os.path.join(output_dir, 'backup/')
    data = [['Time', 'Condition']]
    for i in range(hours):
        row = [datetime.now().strftime('%H:%M:%S.%f'), WEATHER_CONDITIONS[randint(0, len(WEATHER_CONDITIONS)-1)]]
        data.append(row)

    with open(FILE_PATH, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
    shutil.copy(FILE_PATH, BACKUP_PATH)

    return FILE_PATH

def test_task_func():
    # Test with default output directory
    assert task_func(10) == os.path.join(OUTPUT_DIR, 'weather_data.csv')

    # Test with custom output directory
    assert task_func(10, output_dir='./custom_output') == os.path.join('custom_output', 'weather_data.csv')

    # Test with hours less than 1
    with pytest.raises(ValueError):
        task_func(0)

    # Test with hours greater than 1000
    with pytest.raises(ValueError):
        task_func(1001)

    # Test with invalid output directory
    with pytest.raises(FileNotFoundError):
        task_func(10, output_dir='./invalid_output')