import pytest
from src_0360 import task_func
import matplotlib
matplotlib.use('Agg')

@pytest.fixture
def data():
    return {
        'data_dict': {
            'key1': [1, 2, 3, 4, 5],
            'key2': [2, 3, 4, 5, 6]
        },
        'data_keys': ['key1', 'key2']
    }

@pytest.fixture
def expected_output():
    return (1.0, None)

def test_task_func(data, expected_output):
    result = task_func(data['data_dict'], data['data_keys'])
    assert result == expected_output