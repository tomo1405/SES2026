import pytest
from src_0019 import task_func
import os
import glob
import shutil

@pytest.fixture
def setup_test_data(tmpdir):
    # Create a temporary CSV file for testing
    test_file = tmpdir.join('test.csv')
    with open(test_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['Alice', 30])
        writer.writerow(['Bob', 25])
    return str(test_file)

def test_task_func_nonexistent_file():
    result = task_func('nonexistent.csv')
    assert result == []

def test_task_func_non_csv_file(tmpdir):
    test_file = tmpdir.join('test.txt')
    test_file.write('This is a text file.')
    result = task_func(str(test_file))
    assert result == []

def test_task_func_valid_csv(setup_test_data):
    test_file = setup_test_data
    result = task_func(test_file)
    assert len(result) == 5  # Assuming the file is split into 5 parts

    # Clean up split files
    for split_file in result:
        os.remove(split_file)

def test_task_func_shuffled_rows(setup_test_data):
    test_file = setup_test_data
    result = task_func(test_file)
    assert len(result) == 5

    # Read and compare the contents of the split files
    original_content = []
    with open(test_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        original_content.extend(reader)

    for split_file in result:
        with open(split_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            split_content = list(reader)
            assert set(original_content) == set(split_content)  # Ensure all rows are present but order may differ

    # Clean up split files
    for split_file in result:
        os.remove(split_file)

def test_task_func_exception_handling(tmpdir, monkeypatch):
    # Mock subprocess call to raise an exception
    def mock_subprocess_call(*args, **kwargs):
        raise Exception("Mocked exception")

    monkeypatch.setattr(subprocess, 'call', mock_subprocess_call)

    test_file = tmpdir.join('test.csv')
    test_file.write('Name,Age\nAlice,30\nBob,25')
    result = task_func(str(test_file))
    assert result == []

# Clean up any remaining files after tests
@pytest.fixture(autouse=True)
def cleanup():
    yield
    for file in glob.glob('split_*'):
        os.remove(file)