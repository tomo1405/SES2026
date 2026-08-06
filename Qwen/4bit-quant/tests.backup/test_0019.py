import pytest
from src_0019 import task_func

def test_task_func_non_existent_file():
    result = task_func('non_existent.csv')
    assert result == [], "Should return an empty list for non-existent file"

def test_task_func_wrong_extension():
    result = task_func('file.txt')
    assert result == [], "Should return an empty list for non-csv file"

def test_task_func_csv_file(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('subprocess.call', return_value=0)
    mocker.patch('glob.glob', return_value=['split_00', 'split_01', 'split_02', 'split_03', 'split_04'])
    mocker.patch('random.shuffle')
    mocker.patch('csv.reader', return_value=[['header'], ['row1'], ['row2']])
    mocker.patch('csv.writer')

    result = task_func('test.csv')
    assert len(result) == 5, "Should return a list of 5 split files"
    assert all('split_' in f for f in result), "All split files should start with 'split_'"