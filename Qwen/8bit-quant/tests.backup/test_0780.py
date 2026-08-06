import pytest
from src_0780 import task_func

def test_task_func_directory_not_exists():
    non_existent_dir = "/non/existent/directory"
    result, errors = task_func(non_existent_dir)
    assert result is None
    assert len(errors) == 1
    assert errors[0] == f"Directory does not exist: {non_existent_dir}"

def test_task_func_permission_error(mocker):
    existing_dir = "/existing/directory"
    backup_dir = "/fake/backup/path"
    
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock shutil.copytree to raise PermissionError
    mocker.patch('shutil.copytree', side_effect=PermissionError("Permission denied"))
    
    # Mock shutil.rmtree to raise PermissionError
    mocker.patch('shutil.rmtree', side_effect=PermissionError("Permission denied"))
    
    # Mock os.makedirs to do nothing
    mocker.patch('os.makedirs')
    
    result, errors = task_func(existing_dir)
    assert result == backup_dir
    assert len(errors) == 2
    assert errors[0] == "Permission denied"
    assert errors[1] == "Permission denied"

def test_task_func_general_exception(mocker):
    existing_dir = "/existing/directory"
    backup_dir = "/fake/backup/path"
    
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock shutil.copytree to raise a general Exception
    mocker.patch('shutil.copytree', side_effect=Exception("General error"))
    
    # Mock shutil.rmtree to do nothing
    mocker.patch('shutil.rmtree')
    
    # Mock os.makedirs to do nothing
    mocker.patch('os.makedirs')
    
    result, errors = task_func(existing_dir)
    assert result == backup_dir
    assert len(errors) == 1
    assert errors[0] == "General error"

def test_task_func_successful_backup(mocker):
    existing_dir = "/existing/directory"
    backup_dir = "/fake/backup/path"
    
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock shutil.copytree to do nothing
    mocker.patch('shutil.copytree')
    
    # Mock shutil.rmtree to do nothing
    mocker.patch('shutil.rmtree')
    
    # Mock os.makedirs to do nothing
    mocker.patch('os.makedirs')
    
    result, errors = task_func(existing_dir)
    assert result == backup_dir
    assert errors == []

def test_task_func_get_unique_backup_dir(mocker):
    existing_dir = "/existing/directory"
    backup_dir = "/fake/backup/path"
    
    # Mock os.path.exists to return True
    mocker.patch('os.path.exists', return_value=True)
    
    # Mock shutil.copytree to do nothing
    mocker.patch('shutil.copytree')
    
    # Mock shutil.rmtree to do nothing
    mocker.patch('shutil.rmtree')
    
    # Mock os.makedirs to do nothing
    mocker.patch('os.makedirs')
    
    # Mock get_unique_backup_dir to return a specific path
    mocker.patch('src_0780.get_unique_backup_dir', return_value=backup_dir)
    
    result, errors = task_func(existing_dir)
    assert result == backup_dir
    assert errors == []