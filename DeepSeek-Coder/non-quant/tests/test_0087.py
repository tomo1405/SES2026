import pytest
from src_0087 import task_func

def test_task_func():
    result, _ = task_func()
    assert len(result) == 5
    assert all(col in result.columns for col in ['Student', 'Score'])
    assert all(0 <= score <= 100 for score in result['Score'])