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
    assert os.path.isfile(FILE_PATH)
    assert os.path.isdir(BACKUP_PATH)
    assert len(data) == hours
    assert data[0][0] == 'Time'
    assert data[0][1] == 'Condition'
    assert data[1][0] in WEATHER_CONDITIONS
    assert data[1][1] in WEATHER_CONDITIONS
    assert data[2][0] in WEATHER_CONDITIONS
    assert data[2][1] in WEATHER_CONDITIONS
    assert data[3][0] in WEATHER_CONDITIONS
    assert data[3][1] in WEATHER_CONDITIONS
    assert data[4][0] in WEATHER_CONDITIONS
    assert data[4][1] in WEATHER_CONDITIONS
    assert data[5][0] in WEATHER_CONDITIONS
    assert data[5][1] in WEATHER_CONDITIONS
    assert data[6][0] in WEATHER_CONDITIONS
    assert data[6][1] in WEATHER_CONDITIONS
    assert data[7][0] in WEATHER_CONDITIONS
    assert data[7][1] in WEATHER_CONDITIONS
    assert data[8][0] in WEATHER_CONDITIONS
    assert data[8][1] in WEATHER_CONDITIONS
    assert data[9][0] in WEATHER_CONDITIONS
    assert data[9][1] in WEATHER_CONDITIONS

    return FILE_PATH