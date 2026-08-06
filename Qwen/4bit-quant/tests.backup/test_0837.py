import pytest
from src_0837 import task_func
import os
import shutil
import tempfile
import csv

@pytest.fixture
def setup_directories():
    csv_dir = tempfile.mkdtemp()
    processed_dir = tempfile.mkdtemp()
    yield csv_dir, processed_dir
    shutil.rmtree(csv_dir)
    shutil.rmtree(processed_dir)

@pytest.fixture
def create_csv_files(csv_dir):
    filenames = ['file1.csv', 'file2.csv', 'file3.csv']
    for filename in filenames:
        with open(os.path.join(csv_dir, filename), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['332', 'data1'])
            writer.writerow(['444', 'data2'])
    return filenames

def test_task_func(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    filenames = create_csv_files(csv_dir)
    target_value = '332'

    result = task_func(target_value=target_value, csv_dir=csv_dir, processed_dir=processed_dir)

    assert result == {filename: 0 for filename in filenames}
    assert all(os.path.exists(os.path.join(processed_dir, filename)) for filename in filenames)

def test_task_func_simulate(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    filenames = create_csv_files(csv_dir)
    target_value = '332'

    result = task_func(target_value=target_value, csv_dir=csv_dir, processed_dir=processed_dir, simulate=True)

    assert result == {filename: 0 for filename in filenames}
    assert all(os.path.exists(os.path.join(csv_dir, filename)) for filename in filenames)

def test_task_func_no_match(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    filenames = create_csv_files(csv_dir)
    target_value = '999'

    result = task_func(target_value=target_value, csv_dir=csv_dir, processed_dir=processed_dir)

    assert result == {}
    assert all(os.path.exists(os.path.join(processed_dir, filename)) for filename in filenames)

def test_task_func_empty_directory(setup_directories):
    csv_dir, processed_dir = setup_directories
    target_value = '332'

    result = task_func(target_value=target_value, csv_dir=csv_dir, processed_dir=processed_dir)

    assert result == {}
    assert not os.listdir(processed_dir)