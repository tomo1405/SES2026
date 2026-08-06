import pytest
from src_0128 import task_func

@pytest.fixture
def setup():
    return "ROOT_DIR", "DEST_DIR", "SPECIFIC_HASH"

def test_task_func(setup):
    ROOT_DIR, DEST_DIR, SPECIFIC_HASH = setup
    result = task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH)
    assert result == expected_result  # Replace 'expected_result' with the expected result