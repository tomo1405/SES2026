import pytest
from src_0882 import task_func

# Mocking pandas and random for testing purposes
import pandas as pd
import random

@pytest.fixture
def mock_csv_file(tmp_path):
    # Create a temporary CSV file for testing
    csv_content = """index,data
0,a1
1,b2
2,c3
3,d4
4,e5"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)
    return str(csv_file)

def test_task_func_default(mock_csv_file):
    result = task_func(mock_csv_file)
    expected_data = pd.DataFrame({'index': [0, 1, 2, 3, 4], 'data': ['a1', 'b2', 'c3', 'd4', 'e5']})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)

def test_task_func_with_pattern(mock_csv_file):
    result = task_func(mock_csv_file, pattern='[a-z]')
    expected_data = pd.DataFrame({'index': [0, 1, 2, 3, 4], 'data': ['a1', 'b2', 'c3', 'd4', 'e5']})
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_data)

def test_task_func_with_sample_size(mock_csv_file):
    result = task_func(mock_csv_file, sample_size=3)
    assert len(result) == 3

def test_task_func_with_sample_size_larger_than_matches(mock_csv_file):
    result = task_func(mock_csv_file, sample_size=10)
    assert len(result) == 5

def test_task_func_with_different_seed(mock_csv_file):
    result1 = task_func(mock_csv_file, sample_size=3, seed=42)
    result2 = task_func(mock_csv_file, sample_size=3, seed=43)
    pd.testing.assert_frame_equal(result1.reset_index(drop=True), result2.reset_index(drop=True))

def test_task_func_with_no_matches(mock_csv_file):
    result = task_func(mock_csv_file, pattern='[0-9]')
    assert result.empty

def test_task_func_with_nonexistent_column(mock_csv_file):
    with pytest.raises(KeyError):
        task_func(mock_csv_file, column_name='nonexistent')

def test_task_func_with_invalid_csv_file():
    with pytest.raises(FileNotFoundError):
        task_func('nonexistent.csv')