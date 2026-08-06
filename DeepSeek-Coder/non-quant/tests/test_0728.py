import pytest
from src_0728 import task_func

@pytest.fixture
def setup():
    return task_func

def test_task_func(setup):
    func = setup()
    result = func("This is a sentence")
    assert isinstance(result, np.ndarray)
    assert len(result) > 0