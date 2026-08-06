import pytest
from src_0751 import task_func

def test_task_func_empty_df():
    df = pd.DataFrame()
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert results is None

def test_task_func_no_rows_match():
    df = pd.DataFrame({'height': [180, 170, 160], 'weight': [70, 60, 50], 'age': [20, 25, 30]})
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert results is None

def test_task_func_valid_input():
    df = pd.DataFrame({'height': [180, 170, 160], 'weight': [70, 60, 50], 'age': [20, 25, 30]})
    height = 180
    weight = 70
    columns = ['height', 'weight', 'age']
    results = task_func(df, height, weight, columns)
    assert results is not None
    assert results.params['const'] == pytest.approx(0.0)
    assert results.params['height'] == pytest.approx(1.0)
    assert results.params['weight'] == pytest.approx(0.0)
    assert results.params['age'] == pytest.approx(0.0)
    assert results.rsquared == pytest.approx(1.0)