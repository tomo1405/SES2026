import pytest
from src_0595 import task_func
import os
import shutil
import csv

@pytest.fixture(scope='module')
def setup_output_dir(tmpdir_factory):
    dir_path = tmpdir_factory.mktemp('data')
    yield str(dir_path)
    shutil.rmtree(dir_path)

def test_task_func_hours(setup_output_dir):
    hours = 5
    file_path = task_func(hours, output_dir=setup_output_dir)
    assert os.path.exists(file_path)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == hours + 1  # header + data rows
    assert rows[0] == ['Time', 'Condition']

def test_task_func_backup(setup_output_dir):
    hours = 3
    file_path = task_func(hours, output_dir=setup_output_dir)
    backup_path = os.path.join(setup_output_dir, 'backup/weather_data.csv')
    assert os.path.exists(backup_path)
    with open(backup_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == hours + 1  # header + data rows
    assert rows[0] == ['Time', 'Condition']

def test_task_func_default_output_dir(setup_output_dir):
    hours = 2
    file_path = task_func(hours)
    assert os.path.exists(file_path)
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    assert len(rows) == hours + 1  # header + data rows
    assert rows[0] == ['Time', 'Condition']