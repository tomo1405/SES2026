import pytest
from src_0221 import task_func

def test_task_func():
    with pytest.raises(Exception) as excinfo:
        task_func(['red', 'blue', 'green'])
    assert "turtle.Terminator" in str(excinfo.value)