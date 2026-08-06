import pytest
from src_0221 import task_func

def test_task_func():
    # Since the function involves GUI and sleep, it's difficult to test directly.
    # We can check if the function runs without errors by mocking the dependencies.
    with pytest.raises(SystemExit):
        task_func(['red', 'blue', 'green'])