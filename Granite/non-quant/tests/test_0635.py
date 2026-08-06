from itertools import chain
from typing import Any

import numpy as np
import pytest
from scipy import stats


def task_func(input_list: list, repetitions: int) -> Any:
    flattened_list = np.array(list(chain(*[input_list for _ in range(repetitions)])))
    mode = stats.mode(flattened_list)
    return mode

def test_task_func():
    input_list = [1, 2, 3, 4, 5]
    repetitions = 3
    expected_output = stats.mode(np.array(list(chain(*[input_list for _ in range(repetitions)]))))
    actual_output = task_func(input_list, repetitions)
    assert actual_output.mode[0] == expected_output.mode[0] and actual_output.count[0] == expected_output.count[0]

def test_task_func_with_empty_input_list():
    input_list = []
    repetitions = 5
    expected_output = stats.mode(np.array(list(chain(*[input_list for _ in range(repetitions)]))))
    actual_output = task_func(input_list, repetitions)
    assert actual_output.mode[0] == expected_output.mode[0] and actual_output.count[0] == expected_output.count[0]

def test_task_func_with_negative_repetitions():
    input_list = [1, 2, 3, 4, 5]
    repetitions = -1
    with pytest.raises(ValueError) as excinfo:
        task_func(input_list, repetitions)
    assert "Repetitions must be a positive integer" in str(excinfo.value)