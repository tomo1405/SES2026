import matplotlib.pyplot as plt
import pytest
from src_0382 import task_func


# Mocking the file path and content for testing
@pytest.fixture
def mock_file_path(tmpdir):
    file_content = """Index,A,B,C
0,1,2,3
1,4,5,6
2,7,8,9"""
    file_path = tmpdir.join("mock_arena.csv")
    with open(file_path, 'w') as f:
        f.write(file_content)
    return str(file_path)

def test_task_func_with_valid_file(mock_file_path):
    ax, importances = task_func(mock_file_path, target_column='Index', seed=42)
    assert isinstance(ax, plt.Axes)
    assert isinstance(importances, list)
    assert len(importances) == 3  # There are 3 features (A, B, C)

def test_task_func_with_missing_file():
    with pytest.raises(FileNotFoundError) as excinfo:
        task_func('non_existent_file.csv', target_column='Index', seed=42)
    assert "The file 'non_existent_file.csv' does not exist." in str(excinfo.value)

def test_task_func_with_missing_target_column(mock_file_path):
    with pytest.raises(ValueError) as excinfo:
        task_func(mock_file_path, target_column='NonExistentColumn', seed=42)
    assert "The specified target column 'NonExistentColumn' does not exist in the CSV file." in str(excinfo.value)

def test_task_func_with_empty_file(tmpdir):
    empty_file_path = tmpdir.join("empty_arena.csv")
    with open(empty_file_path, 'w') as f:
        pass
    with pytest.raises(ValueError) as excinfo:
        task_func(str(empty_file_path), target_column='Index', seed=42)
    assert "The specified target column 'Index' does not exist in the CSV file." in str(excinfo.value)