import pandas as pd
import pytest
from src_0194 import task_func


@pytest.mark.parametrize("rows, columns", [(10, 5), (20, 10), (50, 20)])
def test_task_func(rows, columns):
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (rows, columns)
    for col in range(columns):
        data_type = choice(DATA_TYPES)
        if data_type == str:
            assert all(isinstance(x, str) for x in df['col' + str(col)])
        elif data_type in [int, float]:
            assert all(isinstance(x, data_type) for x in df['col' + str(col)])
        elif data_type == list:
            assert all(isinstance(x, list) for x in df['col' + str(col)])
        elif data_type == tuple:
            assert all(isinstance(x, tuple) for x in df['col' + str(col)])
        elif data_type == dict:
            assert all(isinstance(x, dict) for x in df['col' + str(col)])
        elif data_type == set:
            assert all(isinstance(x, set) for x in df['col' + str(col)])

def test_task_func_invalid_input():
    with pytest.raises(ValueError):
        task_func(0, 10)
    with pytest.raises(ValueError):
        task_func(10, 0)
    with pytest.raises(ValueError):
        task_func(-1, 10)
    with pytest.raises(ValueError):
        task_func(10, -1)