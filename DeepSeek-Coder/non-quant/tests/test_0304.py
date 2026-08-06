import pytest
from src_0304 import task_func

def test_task_func():
    # Test cases
    # Add your test cases here
    assert task_func("2023-04-01", "UTC", "Europe/Paris") == pytest.approx(0.1, abs=0.1)
    assert task_func("2023-04-01", "UTC", "Europe/Paris") == pytest.approx(0.1, abs=0.1)
    # Add more test cases as needed