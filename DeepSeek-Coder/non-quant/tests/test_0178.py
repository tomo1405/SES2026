import pytest
from src_0178 import task_func
import pandas as pd

@pytest.fixture
def sample_data():
    data = {
        'Title': ['This is a title', 'Another title', 'Yet another title'],
        'Content': ['This is a content', 'Another content', 'Yet another content']
    }
    return pd.DataFrame(data)

def test_task_func(sample_data):
    result = task_func(sample_data)
    assert isinstance(result, dict), "The result should be a dictionary."
    assert len(result) > 0, "The result should not be empty."