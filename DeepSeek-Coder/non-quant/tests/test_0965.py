import pytest
from src_0965 import task_func

@pytest.fixture
def setup():
    return "source_directory", "target_directory"

def test_task_func(setup):
    source_directory, target_directory = setup
    result = task_func(source_directory, target_directory)
    assert result is not None