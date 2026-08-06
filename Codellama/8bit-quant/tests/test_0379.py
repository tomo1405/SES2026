import os
from unittest.mock import patch

from src_0379 import task_func


def test_task_func_valid_input():
    data_dir = './data/'
    data_files = ['file1.csv', 'file2.csv']
    summary_data = [[os.path.basename(file), 10, 5] for file in data_files]
    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    expected_output = table.draw()

    with patch('os.path.exists', return_value=True):
        with patch('glob.glob', return_value=data_files):
            with patch('pd.read_csv', side_effect=summary_data):
                output = task_func(data_dir)
                assert output == expected_output

def test_task_func_invalid_input():
    data_dir = './data/'
    data_files = []
    summary_data = []
    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    expected_output = table.draw()

    with patch('os.path.exists', return_value=True):
        with patch('glob.glob', return_value=data_files):
            with patch('pd.read_csv', side_effect=summary_data):
                output = task_func(data_dir)
                assert output == expected_output

def test_task_func_empty_csv_file():
    data_dir = './data/'
    data_files = ['file1.csv', 'file2.csv']
    summary_data = [[os.path.basename(file), 10, 5] for file in data_files]
    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    expected_output = table.draw()

    with patch('os.path.exists', return_value=True):
        with patch('glob.glob', return_value=data_files):
            with patch('pd.read_csv', side_effect=summary_data):
                output = task_func(data_dir)
                assert output == expected_output

def test_task_func_invalid_csv_file():
    data_dir = './data/'
    data_files = ['file1.csv', 'file2.csv']
    summary_data = [[os.path.basename(file), 10, 5] for file in data_files]
    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)
    expected_output = table.draw()

    with patch('os.path.exists', return_value=True):
        with patch('glob.glob', return_value=data_files):
            with patch('pd.read_csv', side_effect=summary_data):
                output = task_func(data_dir)
                assert output == expected_output