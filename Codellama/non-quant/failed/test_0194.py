import pytest
from src_0194 import task_func


def test_task_func_returns_dataframe():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert isinstance(df, pd.DataFrame)


def test_task_func_returns_correct_shape():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    assert df.shape == (rows, columns)


def test_task_func_returns_correct_data_types():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
    for col in range(columns):
        data_type = choice(DATA_TYPES)
        if data_type == str:
            assert df['col' + str(col)].dtype == object
        elif data_type in [int, float]:
            assert df['col' + str(col)].dtype == data_type
        elif data_type == list:
            assert df['col' + str(col)].dtype == object
        elif data_type == tuple:
            assert df['col' + str(col)].dtype == object
        elif data_type == dict:
            assert df['col' + str(col)].dtype == object
        elif data_type == set:
            assert df['col' + str(col)].dtype == object


def test_task_func_returns_correct_data():
    rows = 10
    columns = 5
    df = task_func(rows, columns)
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