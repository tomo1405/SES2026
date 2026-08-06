import pytest
from src_0801 import task_func, CSV_FILE_PATH, create_test_csv

@pytest.fixture
def setup_test_csv(tmp_path):
    content = [
        ['team', 'goals', 'penalties'],
        ['Team A', '2', '1'],
        ['Team B', '1', '2'],
        ['Team C', '3', '0']
    ]
    test_csv_path = tmp_path / 'test_data' / 'test_case_2.csv'
    test_csv_path.parent.mkdir()
    create_test_csv(test_csv_path, content)
    return test_csv_path

def test_task_func_with_existing_csv(setup_test_csv):
    goals = {'Team D': 4}
    penalties = {'Team D': 1}
    result = task_func(goals, penalties, csv_file_path=str(setup_test_csv))
    assert result == {'goals': 10, 'penalties': 4}

def test_task_func_without_existing_csv(tmp_path):
    goals = {'Team E': 5}
    penalties = {'Team E': 0}
    result = task_func(goals, penalties, csv_file_path=str(tmp_path / 'non_existent.csv'))
    assert result == {'goals': 5, 'penalties': 0}

def test_task_func_with_empty_csv(tmp_path):
    create_test_csv(tmp_path / 'empty.csv', [])
    goals = {'Team F': 6}
    penalties = {'Team F': 2}
    result = task_func(goals, penalties, csv_file_path=str(tmp_path / 'empty.csv'))
    assert result == {'goals': 6, 'penalties': 2}