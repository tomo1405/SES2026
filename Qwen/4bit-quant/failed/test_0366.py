import pytest
from src_0366 import task_func
import os

def test_task_func_valid_n(tmpdir):
    # Arrange
    n = 3
    file_name = str(tmpdir / 'test_file.json')
    
    # Act
    result = task_func(n, file_name)
    
    # Assert
    assert result == file_name
    assert os.path.exists(file_name)
    with open(file_name, 'r') as f:
        data = json.load(f)
        assert len(data) == n
        for word in data:
            assert word in WORDS
            assert isinstance(data[word], int)

def test_task_func_invalid_n():
    # Arrange
    n = 0
    file_name = 'test_file.json'
    
    # Act & Assert
    with pytest.raises(ValueError, match='n must be greater than 0'):
        task_func(n, file_name)

def test_task_func_n_greater_than_word_list_length(tmpdir):
    # Arrange
    n = len(WORDS) + 1
    file_name = str(tmpdir / 'test_file.json')
    
    # Act & Assert
    with pytest.raises(ValueError, match='n must be greater than 0'):
        task_func(n, file_name)

def test_task_func_with_custom_seed(tmpdir):
    # Arrange
    n = 3
    file_name = str(tmpdir / 'test_file.json')
    seed = 42
    
    # Act
    task_func(n, file_name, seed=seed)
    
    # Assert
    with open(file_name, 'r') as f:
        data = json.load(f)
        expected_words = ['date', 'fig', 'elderberry']  # Expected result based on seed 42
        assert list(data.keys()) == expected_words

def test_task_func_file_content(tmpdir):
    # Arrange
    n = 5
    file_name = str(tmpdir / 'test_file.json')
    
    # Act
    task_func(n, file_name)
    
    # Assert
    with open(file_name, 'r') as f:
        data = json.load(f)
        assert len(data) == n
        for word in data:
            assert word in WORDS
            assert data[word] == 1  # Each word should appear once since they are unique in the selection

def test_task_func_overwrites_existing_file(tmpdir):
    # Arrange
    n = 3
    file_name = str(tmpdir / 'test_file.json')
    with open(file_name, 'w') as f:
        json.dump({'apple': 1}, f)
    
    # Act
    task_func(n, file_name)
    
    # Assert
    with open(file_name, 'r') as f:
        data = json.load(f)
        assert len(data) == n
        for word in data:
            assert word in WORDS
            assert isinstance(data[word], int)