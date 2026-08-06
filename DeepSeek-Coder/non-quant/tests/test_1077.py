import pytest
from src_1077 import task_func

@pytest.fixture
def example_data():
    return [
        ("12/01/21 12:34:56.789", "America/New_York"),
        ("01/01/22 00:00:00.000", "Europe/London")
    ]

def test_task_func(example_data):
    result = task_func(example_data[0], example_data[1])
    assert result is not None
    assert len(result) == 2
    assert all(isinstance(row, list) and len(row) == 2 for row in result.values)