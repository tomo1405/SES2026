import pytest
from src_0250 import task_func

def test_task_func():
    train_data, test_data = task_func()
    assert isinstance(train_data, pd.DataFrame)
    assert isinstance(test_data, pd.DataFrame)
    assert len(train_data) == 8000
    assert len(test_data) == 2000
    assert train_data.columns == ['Value']
    assert test_data.columns == ['Value']
    assert train_data.dtypes == ['float64']
    assert test_data.dtypes == ['float64']
    assert train_data.min() >= 0.0
    assert train_data.max() <= 10.0
    assert test_data.min() >= 0.0
    assert test_data.max() <= 10.0