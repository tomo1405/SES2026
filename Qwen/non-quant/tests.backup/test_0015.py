import pytest
from src_0015 import task_func
import os
import shutil
import tempfile

@pytest.fixture
def temp_config_file():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("[Project]\ndirectory=/path/to/project")
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
    with open(os.path.join(temp_project_dir, 'test_file.txt'), 'w') as f:
        f.write('Test content')

    config_content = f"[Project]\ndirectory={temp_project_dir}"
    with open(temp_config_file, 'w') as config_file:
        config_file.write(config_content)

    result = task_func(temp_config_file, archieve_dir=temp_archive_dir)
    assert result is True
    archive_file = f"{temp_archive_dir}/project.zip"
    assert os.path.isfile(archive_file)

def test_task_func_directory_not_exists(temp_config_file):
    config_content = "[Project]\ndirectory=/nonexistent/directory"
    with open(temp_config_file, 'w') as config_file:
        config_file.write(config_content)

    with pytest.raises(FileNotFoundError) as excinfo:
        task_func(temp_config_file)
    assert "Directory /nonexistent/directory does not exist." in str(excinfo.value)

def test_task_func_archive_creation_failure(temp_config_file, temp_project_dir):
    os.makedirs(temp_project_dir)
    with open(os.path.join(temp_project_dir, 'test_file.txt'), 'w') as f:
        f.write('Test content')

    config_content = f"[Project]\ndirectory={temp_project_dir}"
    with open(temp_config_file, 'w') as config_file:
        config_file.write(config_content)

    # Mock shutil.make_archive to fail
    def mock_make_archive(*args, **kwargs):
        raise Exception("Mocked archive creation failure")

    with pytest.raises(Exception) as excinfo:
        with pytest.MonkeyPatch.context() as mp:
            mp.setattr(shutil, 'make_archive', mock_make_archive)
            task_func(temp_config_file)
    assert "Failed to create archive" in str(excinfo.value)