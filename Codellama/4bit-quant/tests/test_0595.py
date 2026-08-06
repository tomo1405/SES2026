import csv
import os
import shutil
from datetime import datetime


def test_task_func():
    hours = 10
    output_dir = './output'
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

    assert os.path.exists(FILE_PATH)
    assert os.path.exists(BACKUP_PATH)
    assert os.path.getsize(FILE_PATH) > 0
    assert os.path.getsize(BACKUP_PATH) > 0

    os.remove(FILE_PATH)
    os.remove(BACKUP_PATH)