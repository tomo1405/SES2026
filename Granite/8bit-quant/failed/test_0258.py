import numpy as np
import math
import pytest
from src_0258 import task_func

@pytest.mark.parametrize("ax, num_turns", [
    (None, 1),
    (None, 2),
    (None, 3),
    (None, 4),
    (None, 5),
])
def test_task_func_valid_input(ax, num_turns):
    assert task_func(ax, num_turns) is not None

@pytest.mark.parametrize("ax, num_turns", [
    (None, -1),
    (None, 0),
    ("invalid", 1),
    (123, 1),
    ([], 1),
    ({}, 1),
])
def test_task_func_invalid_input(ax, num_turns):
    with pytest.raises(Exception):
        task_func(ax, num_turns)