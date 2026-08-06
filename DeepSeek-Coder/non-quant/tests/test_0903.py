import pytest
from src_0903 import task_func

@pytest.fixture
def sample_data():
    data = {
        'x': [1, 2, 3, None, 2],
        'y': [2, 3, None, 1, 2],
        'z': [4, 5, 6, 7, 8]
    }
    return data

def test_task_func(sample_data):
    result = task_func(sample_data)
    expected = {
        'x': Counter({2: 2, 1: 1, 3: 1, None: 1}),
        'y': Counter({2: 2, 3: 1, 1: 1, None: 1}),
        'z': Counter({4: 1, 5: 1, 6: 1, 7: 1, 8: 1})
    }
    assert result == expected