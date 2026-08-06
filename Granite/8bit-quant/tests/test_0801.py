import csv
import os
from collections import Counter
from unittest.mock import patch, mock_open

from src_0801 import task_func

CSV_FILE_PATH = 'match_data.csv'

def create_test_csv(filename, content):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(content)

def setup_csv():
    content = [
        ['team', 'goals', 'penalties'],
        ['Team A', '2', '1'],
        ['Team B', '1', '2'],
        ['Team C', '3', '0']
    ]
    create_test_csv('test_data/test_case_2.csv', content)

def test_task_func_with_no_csv_file():
    goals = {'Team A': 2, 'Team B': 1, 'Team C': 3}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 0}
    expected_counts = Counter({'goals': 6, 'penalties': 3})

    with patch('src_0801.open', mock_open(read_data='')) as mock_file:
        mock_file.return_value.__iter__.return_value = []
        actual_counts = task_func(goals, penalties)

    assert actual_counts == expected_counts

def test_task_func_with_csv_file():
    goals = {'Team A': 2, 'Team B': 1, 'Team C': 3}
    penalties = {'Team A': 1, 'Team B': 2, 'Team C': 0}
    expected_counts = Counter({'goals': 8, 'penalties': 5})

    with patch('src_0801.open', mock_open(read_data='team,goals,penalties\nTeam A,2,1\nTeam B,1,2\nTeam C,3,0\n')):
        actual_counts = task_func(goals, penalties)

    assert actual_counts == expected_counts