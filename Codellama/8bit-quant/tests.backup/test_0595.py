import pytest
from src_0595 import task_func

def test_task_func():
    hours = 10
    output_dir = './output'
    FILE_PATH = os.path.join(output_dir, 'weather_data.csv')
    BACKUP_PATH = os.path.join(output_dir, 'backup/')

    # Test that the function returns the correct file path
    assert task_func(hours, output_dir) == FILE_PATH

    # Test that the file is created and has the correct contents
    with open(FILE_PATH, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) == hours + 1
        assert data[0] == ['Time', 'Condition']
        for i in range(1, len(data)):
            assert data[i][0] == datetime.now().strftime('%H:%M:%S.%f')
            assert data[i][1] in WEATHER_CONDITIONS

    # Test that the backup file is created and has the correct contents
    assert os.path.exists(BACKUP_PATH)
    with open(BACKUP_PATH, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) == hours + 1
        assert data[0] == ['Time', 'Condition']
        for i in range(1, len(data)):
            assert data[i][0] == datetime.now().strftime('%H:%M:%S.%f')
            assert data[i][1] in WEATHER_CONDITIONS