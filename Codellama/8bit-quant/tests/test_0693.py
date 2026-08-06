import pytest
from src_0693 import task_func
import math
import pandas as pd

def test_task_func():
    tuples_list = [(1, 2), (3, 4), (5, 6)]
    expected_result = pd.DataFrame([(math.sin(1), math.sin(2)), (math.sin(3), math.sin(4)), (math.sin(5), math.sin(6))])
    result = task_func(tuples_list)
    assert result.equals(expected_result)