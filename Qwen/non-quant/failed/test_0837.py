import pytest
from src_0837 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def setup_directories():
    # Create temporary directories for csv_files and processed_files
    csv_dir = tempfile.mkdtemp()
    processed_dir = tempfile.mkdtemp()
    yield csv_dir, processed_dir
    # Clean up directories after tests
    shutil.rmtree(csv_dir)
    shutil.rmtree(processed_dir)

@pytest.fixture
def create_csv_files(csv_dir):
    # Create sample CSV files in the csv_dir
    data = [
        ("file1.csv", [["123", "data1"], ["332", "data2"]]),
        ("file2.csv", [["456", "data3"], ["789", "data4"]]),
        ("file3.csv", [["332", "data5"], ["678", "data6"]])
    ]
    for filename, rows in data:
        with open(os.path.join(csv_dir, filename), 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def test_task_func(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    result = task_func(target_value='332', csv_dir=csv_dir, processed_dir=processed_dir, simulate=False)
    expected_result = {
        'file1.csv': 1,
        'file3.csv': 0
    }
    assert result == expected_result
    # Check if files have been moved to the processed directory
    assert 'file1.csv' in os.listdir(processed_dir)
    assert 'file2.csv' in os.listdir(csv_dir)
    assert 'file3.csv' in os.listdir(processed_dir)

def test_task_func_simulate(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    result = task_func(target_value='332', csv_dir=csv_dir, processed_dir=processed_dir, simulate=True)
    expected_result = {
        'file1.csv': 1,
        'file3.csv': 0
    }
    assert result == expected_result
    # Check if files have not been moved to the processed directory
    assert 'file1.csv' in os.listdir(csv_dir)
    assert 'file2.csv' in os.listdir(csv_dir)
    assert 'file3.csv' in os.listdir(csv_dir)

def test_task_func_no_match(setup_directories, create_csv_files):
    csv_dir, processed_dir = setup_directories
    result = task_func(target_value='999', csv_dir=csv_dir, processed_dir=processed_dir, simulate=False)
    expected_result = {}
    assert result == expected_result
    # Check if no files have been moved to the processed directory
    assert 'file1.csv' in os.listdir(csv_dir)
    assert 'file2.csv' in os.listdir(csv_dir)
    assert 'file3.csv' in os.listdir(csv_dir)