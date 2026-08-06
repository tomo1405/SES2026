import pytest
from src_0120 import task_func

def test_task_func():
    # Call the function
    task_func()

    # Use pytest.raises to check if an exception is raised
    with pytest.raises(Exception) as exc_info:
        # Call the function with invalid arguments
        task_func(invalid_argument='invalid')

    # Assert that the correct exception is raised
    assert exc_info.type is TypeError