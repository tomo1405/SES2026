import pytest
from src_0008 import task_func

@pytest.fixture
def sample_data():
    return [
        "product1,10",
        "product2,20",
        "product1,30",
        "product3,15"
    ]

@pytest.fixture
def csv_file(tmp_path, sample_data):
    file_path = tmp_path / "test.csv"
    with open(file_path, 'w') as f:
        f.write("\n".join(sample_data))
    return file_path

def test_task_func(csv_file):
    result = task_func(csv_file)
    assert result == "product1"