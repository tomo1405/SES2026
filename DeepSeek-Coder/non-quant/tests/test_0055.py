import pytest
from src_0055 import task_func

@pytest.fixture
def sample_text():
    return "This is a sample text. This text is for testing. It contains multiple sentences."

def test_task_func(sample_text):
    result = task_func(sample_text)
    assert result is not None
    assert isinstance(result, pd.DataFrame)
    assert not result.empty