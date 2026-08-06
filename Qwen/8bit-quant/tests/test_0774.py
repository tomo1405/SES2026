import pytest
from src_0774 import task_func
import os
import shutil
from unittest.mock import patch, MagicMock

@pytest.fixture
def setup_directories(tmp_path):
    source_dir = tmp_path / 'source'
    target_dir = tmp_path / 'target'
    source_dir.mkdir()
    target_dir.mkdir()
    
    # Create some test files in the source directory
    (source_dir / 'test-1.json').touch()
    (source_dir / 'test-2.json').touch()
    (source_dir / 'notmatching.txt').touch()
    
    return source_dir, target_dir

@patch('os.listdir')
@patch('shutil.move')
def test_task_func(mock_move, mock_listdir, setup_directories):
    source_dir, target_dir = setup_directories
    
    # Mock os.listdir to return the files in the source directory
    mock_listdir.return_value = ['test-1.json', 'test-2.json', 'notmatching.txt']
    
    # Call the function
    task_func()
    
    # Check that shutil.move was called correctly
    mock_move.assert_has_calls([
        pytest.call(os.path.join(source_dir, 'test-1.json'), os.path.join(target_dir, 'test.json')),
        pytest.call(os.path.join(source_dir, 'test-2.json'), os.path.join(target_dir, 'test.json'))
    ], any_order=True)
    
    # Ensure that only the matching files were moved
    assert not (source_dir / 'test-1.json').exists()
    assert not (source_dir / 'test-2.json').exists()
    assert (target_dir / 'test.json').exists()
    assert (source_dir / 'notmatching.txt').exists()

@patch('os.listdir')
@patch('shutil.move')
def test_task_func_no_matching_files(mock_move, mock_listdir, setup_directories):
    source_dir, target_dir = setup_directories
    
    # Mock os.listdir to return no matching files
    mock_listdir.return_value = ['notmatching1.txt', 'notmatching2.txt']
    
    # Call the function
    task_func()
    
    # Check that shutil.move was not called
    mock_move.assert_not_called()
    
    # Ensure that no files were moved
    for file in ['notmatching1.txt', 'notmatching2.txt']:
        assert (source_dir / file).exists()
        assert not (target_dir / file).exists()

@patch('os.listdir')
@patch('shutil.move')
def test_task_func_empty_source_directory(mock_move, mock_listdir, setup_directories):
    source_dir, target_dir = setup_directories
    
    # Mock os.listdir to return an empty list
    mock_listdir.return_value = []
    
    # Call the function
    task_func()
    
    # Check that shutil.move was not called
    mock_move.assert_not_called()
    
    # Ensure that no files were moved
    assert not any(file.exists() for file in target_dir.iterdir())