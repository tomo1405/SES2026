import pandas as pd
import seaborn as sns
import pytest

from src_0417 import task_func

@pytest.fixture
def input_data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def test_task_func(input_data):
    result = task_func(input_data)
    assert result is not None
    assert isinstance(result, sns.matrix.Matrix)

def test_task_func_with_invalid_column(input_data):
    result = task_func(input_data, column="invalid_column")
    assert result is None

def test_task_func_with_no_number_columns(input_data):
    data = pd.DataFrame(input_data)
    data["category"] = ["A", "B", "C"]
    result = task_func(data)
    assert result is None