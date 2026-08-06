import pytest
from src_1022 import task_func

def test_task_func():
    input_string = "Hello, world!"
    verify_hash = "7509e5bda0c762d2bac7f90d758b5b2263fa01ccbc542ab5e3df163be08e6ca9"
    result = task_func(input_string, verify_hash)
    assert result == verify_hash

    input_string = 123
    with pytest.raises(TypeError):
        task_func(input_string, verify_hash)

    input_string = "Hello, world!"
    verify_hash = 123
    with pytest.raises(TypeError):
        task_func(input_string, verify_hash)