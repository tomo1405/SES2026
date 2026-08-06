import pytest
from src_0650 import task_func

@pytest.fixture
def dates_str_list():
    return ["2023-04-01", "2023-04-02", "2023-04-03", "2023-04-04", "2023-04-05"]

def test_task_func(dates_str_list):
    result = task_func(dates_str_list)
    assert isinstance(result, pd.Series)
    assert len(result) == 7
    assert all(isinstance(count, int) for count in result)