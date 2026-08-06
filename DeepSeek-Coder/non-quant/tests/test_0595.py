import pytest
from src_0595 import task_func

@pytest.fixture
def setup_and_teardown():
    yield

def test_task_func(setup_and_teardown):
    hours = 5
    output_dir = './output'
    result = task_func(hours, output_dir=output_dir)
    assert os.path.exists(result)
    assert os.path.isfile(result)
    with open(result, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        assert len(data) == hours + 1  # +1 for the header
        assert data[0] == ['Time', 'Condition']
        for row in data[1:]:
            assert len(row) == 2
            assert row[0].isdigit()
            assert row[1] in ['Sunny', 'Cloudy', 'Rainy', 'Snowy', 'Stormy']