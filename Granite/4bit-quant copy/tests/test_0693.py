import pytest
from src_0693 import task_func
import math
import pandas as pd

@pytest.mark.parametrize("tuples_list, expected_output", [
    ([(1, 2, 3)], pd.DataFrame([(math.sin(n) for n in (1, 2, 3))])),
    ([(4, 5, 6), (7, 8, 9)], pd.DataFrame([(math.sin(n) for n in (4, 5, 6)), (math.sin(n) for n in (7, 8, 9))])),
])
def test_task_func(tuples_list, expected_output):
    assert task_func(tuples_list).equals(expected_output)