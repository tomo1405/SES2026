import pytest
from src_0421 import task_func

def test_task_func():
    data = {
        "column1": [1, 2, 3],
        "column2": [4, 5, 6],
        "column3": ["a", "b", "c"],
    }
    expected_result = {
        "column1": [-1.22474487, -0.4472136, 1.22474487],
        "column2": [-1.22474487, -0.4472136, 1.22474487],
        "column3": ["a", "b", "c"],
    }
    result = task_func(data)
    assert result.equals(expected_result)

if __name__ == "__main__":
    pytest.main()