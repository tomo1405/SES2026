import pytest
from src_0015 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def temp_config_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp_file:
        temp_file.write("[Project]\ndirectory = /tmp/project")
    yield temp_file.name
    os.remove(temp_file.name)

@pytest.fixture
def temp_project_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

@pytest.fixture
def temp_archive_dir():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)

def test_task_func_success(temp_config_file, temp_project_dir, temp_archive_dir):
    os.makedirs(temp_project_dir)
    assert task_func(temp_config_file, archieve_dir=temp_archive_dir) == True
    archive_file = f"{temp_archive_dir}/project.zip"
    assert os.path.isfile(archive_file)

def test_task_func_directory_not_exists(temp_config_file, temp_archive_dir):
    with pytest.raises(FileNotFoundError):
        task_func(temp_config_file, archieve_dir=temp_archive_dir)

def test_task_func_archive_creation_failure(temp_config_file, temp_project_dir, temp_archive_dir):
    os.makedirs(temp_project_dir)
    def mock_make_archive(*args, **kwargs):
        raise Exception("Mocked archive creation failure")
    shutil.make_archive = mock_make_archive
    with pytest.raises(Exception) as excinfo:
        task_func(temp_config_file, archieve_dir=temp_archive_dir)
    assert str(excinfo.value) == "Mocked archive creation failure"

def test_task_func_default_archive_dir(temp_config_file, temp_project_dir):
    os.makedirs(temp_project_dir)
    assert task_func(temp_config_file) == True
    default_archive_dir = '/home/user/archive'
    archive_file = f"{default_archive_dir}/project.zip"
    assert os.path.isfile(archive_file)