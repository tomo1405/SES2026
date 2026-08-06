import pandas as pd
import pytest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from src_0879 import task_func

@pytest.fixture
def data():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

@pytest.fixture
def target():
    return "target"

def test_task_func_with_valid_data(data, target):
    mse, model, data = task_func(data, target)
    assert isinstance(mse, float)
    assert isinstance(model, RandomForestRegressor)
    assert isinstance(data, pd.DataFrame)

def test_task_func_with_empty_data(target):
    with pytest.raises(ValueError) as excinfo:
        task_func([], target)
    assert "Data must not be empty and target column must exist in the DataFrame." in str(excinfo.value)

def test_task_func_with_invalid_target(data):
    with pytest.raises(ValueError) as excinfo:
        task_func(data, "invalid_target")
    assert "Data must not be empty and target column must exist in the DataFrame." in str(excinfo.value)

def test_task_func_with_test_size_and_random_state(data, target):
    mse1, model1, data1 = task_func(data, target, test_size=0.2, random_state=42)
    mse2, model2, data2 = task_func(data, target, test_size=0.2, random_state=42)
    assert mse1 == mse2
    assert model1 != model2
    assert data1 is not data2